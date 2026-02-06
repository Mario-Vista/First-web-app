from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import auth
import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class Utente(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(request: Utente):
    return auth.login(request.username,request.password)

@app.post("/signup")
def login(request: Utente):
    return auth.sign_up(request.username,request.password)



if __name__ == "__main__": 
    init_db.init_database()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


