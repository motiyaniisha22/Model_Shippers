from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def index():
    return {"message":"Hello World"}
@app.get("/test")
def test():
    a=10
    b=20
    c = a+b
    return {"message":"Test API","total":c}