from pydantic import BaseModel


#Create a product mode with id , name , price and stock


class product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool

input_data={'id':101,'name':'rai','price':40.4, 'in_stock':True}

user=product(**input_data)


print(user)