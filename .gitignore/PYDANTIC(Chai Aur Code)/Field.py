from pydantic import  BaseModel,Field
from typing import Dict,List,Optional

class Cart(BaseModel):
    id:int
    item:list[str]
    quantities:Dict[str,int]


class BlogPost(BaseModel):
    title:str
    content:str
    image_URL:Optional[str]=None



## Create employee basemode with field

class employee(BaseModel):
    id:int
    name:str=Field(...,
                   min_length=3,
                   max_length=1000,
                   description="enter employee name",
                   examples="rai")
    Department:Optional[str]='General'
    Salary:float=Field(...,
                       gt=1000,
                       example='50000',
                       description="enter salary")
    
