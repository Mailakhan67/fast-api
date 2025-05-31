from pydantic import BaseModel ,configDict
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
    createdAt : datetime
    address:Address
    tags:List[str]=[]
    model_config=configDict(
        json_encoders={datetime:lambda v : v.strftime(
            '%d-%m-%Y %H:%M:%S'
        )}
    )


#create a user instance
user=User(
    id=3,
    name='maila',
    email="mailakhan66@gmail.com",
    is_active=True,
    created_at=datetime(2024, 3,15,14,30),
    address=Address(
        street='123 something',
        city='Karachi',
         zip_code='001144',
    ),
    is_active=True,
    tags=['premium', ' subscriber'],
) ,  



# using model_dump -> dict
python_dict=user.model_dump()
print(python_dict)

#using model_dump_json
json_str=user.model_dump_json()