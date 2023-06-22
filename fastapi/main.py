from fastapi import FastAPI 

app = FastAPI()

users = {
    1: {
        "id":1,
        "name": "John Doe",
        "city": "Ahmedabad",
        "email": "john.doe@emailinator.com"
    },
    2: {
        "id":2,
        "name": "Jane Doe",
        "city": "Gandhinagar",
        "email": "jane.doe@emailinator.com"
    },
    3: {
        "id":3,
        "name": "Jack Doe",
        "city": "Baroda",
        "email": "jack.doe@emailinator.com"
    }
}
@app.get("/hello") #http://localhost"8000 GET
def index():
    return { "message": "Hello World!"}

@app.get("/test") #http://localhost"8000 GET
def index():
    a = 10
    b = 20
    c = a + b 
    return { "message" : "Test API", "Total" : c }

@app.get("/users/")
def get_users(city: str = None):
    return { "message": "Users list", "data": users, "filter": city }

@app.get("/users/{user_id}")  # GET baseUrl/users/1
def get_user_by_id(user_id: int, city: str):
    return { "message": "User detail", "data": users[user_id], "filter": city }


