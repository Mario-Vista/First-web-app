from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import auth
import init_db

# Initialize FastAPI application
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
# This allows frontend applications running on different origins
# to make requests to this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (for development)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"]   # Allow all headers
)


# Pydantic model for request body
# This ensures that incoming JSON has 'username' and 'password'
class Utente(BaseModel):
    username: str
    password: str


# Login endpoint
# Receives a POST request with a username and password
# Calls the 'login' function from auth.py
@app.post("/login")
def login(request: Utente):
    return auth.login(request.username, request.password)


# Signup endpoint
# Receives a POST request with a username and password
# Calls the 'sign_up' function from auth.py
@app.post("/signup")
def signup(request: Utente):
    return auth.sign_up(request.username, request.password)


# Main entry point
if __name__ == "__main__":
    # Initialize the database (create tables if not exists)
    init_db.init_database()

    # Run the FastAPI application with Uvicorn
    # host="0.0.0.0" makes the server accessible externally
    # reload=True enables auto-reload during development
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
