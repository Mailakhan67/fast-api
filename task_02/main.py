from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Student(BaseModel):
    id : int
    name : str
    roll_num : int

students :List[Student]=[]

# Get endpoint
@app.get("/")
def read_root():
    return {"greeting":"hello from maila"}

@app.get("/students")
def get_students():
    return students


@app.post("/students")
def add_student(student : Student):
    students.append(student)
    return student


@app.put("/students/{student_id}")
def update_student(student_id : int , updated_student :Student):
    for index, Student in enumerate(students):
        if Student.id == student_id:
            students[index]=update_student
            return update_student
        return {"error" : " student not found"}
    

@app.delete("/students/ {student_id}")
def delete_student(student_id : int):
      for index, Student in enumerate(students):
          if Student.id == student_id:
                deleted= students.pop(index)
                return deleted
      return {"error" : " student not found"}