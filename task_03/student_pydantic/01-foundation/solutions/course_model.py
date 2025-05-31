from pydantic import BaseModel, Field
from typing import List,Dict,Optional

class Lesson(BaseModel):
    lession_id:str
    topic:str



class Module(BaseModel):
      module_id:int
      name:str
      lessons:List[Lesson]


class Course(BaseModel):
    course_id:int
    title:str
    modules:List[Module]

