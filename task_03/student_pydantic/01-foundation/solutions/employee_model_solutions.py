from pydantic import BaseModel, Field
from typing import List,Dict,Optional


class Employee(BaseModel):
    id:int
    name:str = Field(...,min_length=3 , max_length=50,description='employee nmae', example='maila ameen')
    department:Optional[str]='General'
    salary:float = Field(...,ge=10000)