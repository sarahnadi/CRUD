from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

users = {
        1:{
            "name":"john",
            "age": 17,
            "year": "year 12"
            }
        }
class User(BaseModel):
    name: str
    age: int
    year: str
class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return{"name": "First Data"}
@app.get("/get-user/{user_id}")
def get_user(user_id: int = Path(description="The ID of the user you want to view")):
    return users[user_id]

@app.get("/get-by-name")
def get_user(name : str):
    for user_id in users:
        if users[user_id]["name"] == name:
            return users[user_id]
        return {"Data": "Not Found"}
@app.post("/create-user/{user_id}")
def create_user(user_id : int, user : User):
    if user_id in users:
        return{"Error": "User already exists"}
    users[user_id] = user
    return user[user_id]
@app.put("/update-user/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        return{"Error": "User does not exist"}
    
    if user.name != None:
        users[user_id].name = user.name
    if users.age != None:
        users[user_id].age = user.age
    if user.year != None:
        users[user_id].year = user.year
    return users[user_id]

@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        return{"Error": "User does not exist"}
    del users[user_id]
    return{"Message": "User deleted successfully"}
