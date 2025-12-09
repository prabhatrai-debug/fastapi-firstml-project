from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd
from enum import Enum

with open('model.pkl','rb') as f:
    model=pickle.load(f)

app=FastAPI()

class CountryCode(str, Enum):
    IN = "IN"
    US = "US"
    UK = "UK"
    CA = "CA"
    AU = "AU"
    SG = "DE"
##Pydantic model to to validate incoming data 
class UserInput(BaseModel):
    gender:Annotated[str,Field(...,description='gender of the user',example="Male")]
    age:Annotated[int,Field(...,gt=0 ,lt=120,description='Age of the user')]                
    country:Annotated[CountryCode,Field(...,description='country of the user( IN, US, UK, CA, AU, SG))', example="IN")]                    
    listening_time:Annotated[int,Field(...,gt=0 ,lt=250,description='listening_time of the user(in min)')]
    songs_played_per_day:Annotated[int,Field(...,gt=0 ,lt=30,description='songs_played_per_day by the user')]    
    skip_rate:Annotated[float,Field(...,description='skip_rate of the user',example= 0.2)]               
    device_type:Annotated[Literal['Desktop','Web','Mobile'],Field(...,description='which device used by the user(Desktop,Web,Mobile)')]             
    offline_listening:Annotated[int,Field(...,description='is user listen offline(1/0)',example=1)]
    

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
@app.post("/predict")
def predict_premium(data:UserInput):
  
   input_df=pd.DataFrame([{
        'gender':data.gender,
        'country':data.country,
        'listening_time':data.listening_time,
        'skip_rate':data.skip_rate,
        'device_type':data.device_type,
        'age_group':data.age_group,
        'offline_listening':data.offline_listening,
        'songs_played_per_day':data.songs_played_per_day

  }])
   
   prediction=model.predict(input_df)[0]

   return JSONResponse(status_code=200,content={'subscription_type':prediction})
