from fastapi import FastAPI,Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserSignup(BaseModel):
    user:str
    email:EmailStr
    password:str


class Settings(BaseModel):
    app_name:str='my app'
    admin_email:str="mailakhan815@gmqail.com"



def get_settings():
    return Settings()



@app.post('/signup')
def signup(user:UserSignup):
    return {'message' : f'user {user.user} signed up successfully'}

@app.get('/settings')
def get_settings_endpoint(settings:Settings=Depends(get_settings)):
    return settings


