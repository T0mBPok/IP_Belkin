from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.users.router import router as user_router
from src.data.router import router as data_router

app = FastAPI(title="IP_belkin")
PORT=8080
HOST = "127.0.0.1"

app.include_router(user_router)
app.include_router(data_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run('src.main:app', host = HOST, port=PORT, reload = True)