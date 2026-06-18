from fastapi import FastAPI
from pydantic import BaseModel # Step A: Import BaseModel

app = FastAPI()

# Step B: Define your data structure using a class
class User(BaseModel):
    name: str
    age: int

# Step C: Pass the Pydantic model into your route
@app.post("/create_user")
def create_user(user: User): # Expect a full JSON body matching the User class
    return {
        "message": "User created",
        "data": user
    }