from fastapi import FastAPI
from .routers import auth, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Planner API"}
