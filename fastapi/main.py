from fastapi import FastAPI  # importing packages

app = FastAPI()  # creating an instance

@app.get("/") # @ is decorator in python  / means serving with the base URL

# listen for an http request that comes from base URL (http://localhost:8000) with the GET method
def index():    # function which returns a dictionary with a key and a value.
    return {"message": "Hello World"}

@app.get("/test") # http://localhost:8000 GET
def index():   
    a = 10
    b = 20
    c = a+b
    return {"message": "Test API", "total":c}
