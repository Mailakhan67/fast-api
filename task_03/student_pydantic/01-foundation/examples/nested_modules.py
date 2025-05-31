from pydantic import BaseModule 
from typing import List,Optional

class Address(BaseModule):
    street:str
    city:str
    postal_code:str


class User(BaseModel):
    id:int
    name:str
    address:Address


class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None


Comment.model_rebuild()

address=Address(
    street="123 something",
    city="karachi",
    postal_code=10001,
)


user=User(
    id=1,
    name='maila',
    address=address,
)

comment=Comment(
    id=1,
    content='first comment'
    replies=[
        Comments(id=2,content='reply1')
        Comments(id=3,content='reply2')
    ]
)