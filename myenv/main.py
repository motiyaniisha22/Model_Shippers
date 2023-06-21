from fastapi import FastAPI 

app = FastAPI()

@app.get("/hello") #http://localhost"8000 GET
def index():
    return { "message": "Hello World!"}

@app.get("/test") #http://localhost"8000 GET
def index():
    a = 10
    b = 20
    c = a + b 
    return { "message" : "Test API", "Total" : c }