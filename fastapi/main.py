from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Annotated, Optional
from sqlmodel import SQLModel, Field, create_engine, Session, update

app = FastAPI()

DATABASE_URL = 'postgresql://postgres:dhruvi@localhost/ML_Model'

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city: str
    email: str 

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

users = {
    1: {
        "id": 1,
        "name": "John Doe",
        "city": "Ahmedabad",
        "email": "john.doe@mailinator.com"
    },
    2: {
        "id": 2,
        "name": "John Doe",
        "city": "Gandhinagar",
        "email": "john.doe@mailinator.com"
    },
    3: {
        "id": 3,
        "name": "John Doe",
        "city": "Rajkot",
        "email": "john.doe@mailinator.com"
    },
    4: {
        "id": 4,
        "name": "John Doe",
        "city": "Baroda",
        "email": "john.doe@mailinator.com"
    }
}

class User(BaseModel):
    id: int
    name: str
    city: str
    email: str

class UserUpdate(BaseModel):
    name: str
    city: str
    email: str

@app.get("/hello") # http://localhost:8000/hello GET
def index():
    return { "message": "Hello World" }

@app.get("/test") # http://localhost:8000/hello GET
def test():
    a = 10
    b = 20
    c = a + b
    return { "message": "Test API", "total": c }

@app.get("/users", status_code=200)
def get_users(x_api_key: Annotated[str | None, Header()] = None, city: str = None):
    with Session(engine) as session:
        users = session.query(Users).all() # select * from users
        print(f'Users list {users}')
        return { "message": "Users List", "data": users, "header": x_api_key }

@app.get("/users/{user_id}") # GET baseUrl/users/1
def get_user_by_id(user_id: int, city: str):
    return { "message": "User detail", "data": users[user_id] } 

@app.post("/users")
def create_user(user: User):
    users.update({user.id: user})
    return { "message": "New user", "data": user }

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    if user_id not in users.keys():
        return { "message": "Invalid User Id"}

    updated_user = users.get(user_id)
    updated_user.update({ "name": user.name })
    updated_user.update({ "city": user.city })
    updated_user.update({ "email": user.email })
    users.update({ user_id: updated_user})

    return {"message": "User details updated successfully", "data": updated_user }

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users.keys():
        return{ "message": "Invalid User Id"}
    
    del users[user_id]
    return {"message": "User deleted successfully", "data": users}
