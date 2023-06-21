from fastapi import FastAPI

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
    return { "message": "Users List", "data": users, "filter":city }

@app.get("/users/{user_id}") # GET baseUrl/users/1
def get_user_by_id(user_id: int, city: str):
    return { "message": "User detail", "data": users[user_id] } 
