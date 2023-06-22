from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/users")
def get_users(city: str = None):
    if city is None:
        return { "message": "Users List", "data": list(users.values()) }
    
    filtered_users = [user for user in users.values() if user.get('city').lower() 
    == city.lower()]
    return { "message": "Users List", "data": filtered_users}

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
