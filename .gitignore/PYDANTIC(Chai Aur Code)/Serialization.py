from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool=True
    createdAt:datetime
    address:Address
    tags:List[str]=[]

    model_config=ConfigDict(                     ##to read the date-time properly in output
        json_encoders={datetime:lambda v:v.strftime('%d-%m-%Y  %H:%M:%S')}  
    )

user=User(
    id=1,
    name="rai",
    email="pr@gmail.com",
    is_active=False,
    createdAt=datetime(2025,3,15,14,30),
    address=Address(
        street="xyz",
        city="azm",
        zip_code="1002",
    ),
    tags=["Premium","subscriber"]

)


#using model_dump->dict

python_dict=user.model_dump()
print(python_dict)
print("==============================\n")
#using model_dump_json

json_str=user.model_dump_json()
print(json_str)
