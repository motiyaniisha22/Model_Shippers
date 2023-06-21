from fastapi import FastAPI
#creating an instance
app = FastAPI()
# @-- sign of decorator
@app.get("/hello")  # "/" defining the end point/base url after /hello i'm serving to the string 
# decorating the function using decorator and keyword get maps to http verb get
#listen for an http request that comes from the base URL http://locahost:8000 with the GET method
#python function
def index(): 
    return {"message":"Hello World"} #dictionary

@app.get("/test")

def test(): 
    a = 10
    b = 20
    c = a + b
    return {"message":"Test API", "total": c}
