from typing import List
from pydantic import BaseModel, Field, EmailStr
from datetime import date


class PostSchema(BaseModel):
    id : int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo" : {
                "title" : "some title about cars",
                "content": "some content about cars"
            }
        }

class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "name": "Duo",
                "email":"help@duoduo.com",
                "password":"123"
            }
        }
class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "email":"help@duoduo.com",
                "password":"123"
            }
        }