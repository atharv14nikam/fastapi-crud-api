from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Welcome Home"}

@app.get("/about")
def about():
    return {"Message": "This is the about page"}

@app.get("/contact")
def contact():  
    return {"Message": "This is the contact page"}

@app.get("/New")
def new():
    return{"Message":"Naya hain yain"}


#dynamic endpoint:
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return{"user_id":user_id}
