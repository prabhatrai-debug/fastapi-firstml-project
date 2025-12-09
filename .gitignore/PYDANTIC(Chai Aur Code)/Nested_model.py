from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address    #This class is refrencing Address Class

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None   #since it is refrencing comment class itself 
                                             #isko hume rebuild karna hi padega tab koi error nhi aayega

Comment.model_rebuild()

address=Address(
    street="23",
    city='azm',
    postal_code="1002"
)

user=User(
    id=26,
    name="rai",
    address=address
)

comment=Comment(
    id=87,
    content="this is my first comment",
    replies=[
        Comment(id=1,content='reply1'),
        Comment(id=2,content='reply2')
    ]
)

print(comment)
print(user)