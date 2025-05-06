import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from App.api.v1.endpoint.auth import auth_api
from fastapi.responses import RedirectResponse


base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, "App", "config", ".env"))

app = FastAPI()

HOST = os.getenv("HOST","0.0.0.0")
PORT = os.getenv("PORT","8000")

app.include_router(auth_api.router)

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=int(PORT), log_level="debug")