from fastapi import FastAPI,Path,HTTPException,Query
import json

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
        return data
    
@app.get('/view')
def view():
        data=load_data()
        return data    


#to view data the data of specific  patient 
#PATH parameter


@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='ID of the patient' , example='P001')): 
     
     data=load_data()

     if patient_id in data:
          return data[patient_id]
     raise HTTPException(status_code=404, detail='Patient not found')
     

 #QUERY parameter---->> To view the sorted data 
@app.get('/sort')
def sort_patients(sort_by:str= Query(..., description='sort on the basis of height,weight or bmi'),order:str=Query('asc',descripton='sort in asc or dsc order')):
     
     valid_fields=['height','weight','bmi']

     if sort_by not in valid_fields:
       raise HTTPException(status_code=400,detail=f'Invalid fields select from {valid_fields}')

     if order not in ['asc','dsc']:
          raise HTTPException(status_code=400,detail='Invalid oreder select between asc and dsc')
     
     data=load_data()

     sort_order=True if order=='dsc' else False

     sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

     return sorted_data
     