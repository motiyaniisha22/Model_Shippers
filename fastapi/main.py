<<<<<<< HEAD
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
=======
# importing package
from fastapi import FastAPI

# creating an instance
app = FastAPI()

# '@' represents decorator with http method/verb by defining a path
# listen for an http request that comes for base url (http://localhost:8000) with the GET method
@app.get("/")

#@app.get("/hello")
# a fucntion which returns a dictionary with a key and a value. We decorate this function
def index():
    return {"message" : "Hello World"}


@app.get('/test')
def index():
    a = 10
    b = 20
    c = a + b
    return {'message' : "Test API" , 'total' : c}
>>>>>>> 505bd39c1dd6e4565fecc0479d95c50d9a36e71f
