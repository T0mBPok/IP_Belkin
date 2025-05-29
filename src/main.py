from fastapi import FastAPI
import uvicorn
from src.users.router import router as user_router
from src.data.router import router as data_router

app = FastAPI(title="IP_belkin")
PORT=8080

app.include_router(user_router)
app.include_router(data_router)

if __name__ == "__main__":
    uvicorn.run('src.main:app', host = '127.0.0.1', port=PORT, reload = True)