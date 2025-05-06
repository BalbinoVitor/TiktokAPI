from App.config.logs import setup_logging
import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from App.api.v1.endpoint.auth import auth_api
from App.api.v1.endpoint.actions import actions_api
from App.api.v1.endpoint.extraction import extraction_api
from App.api.v1.endpoint.monitor import monitor_api
from App.api.v1.endpoint.posts import posts_api
from App.api.v1.endpoint.sessions import sessions_api
from App.api.v1.endpoint.upload import upload_api
from fastapi.responses import RedirectResponse

logger = setup_logging()

base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, "App", "config", ".env"))

app = FastAPI()

HOST = os.getenv("HOST","0.0.0.0")
PORT = os.getenv("PORT","8000")

app.include_router(auth_api.router)
app.include_router(actions_api.router)
app.include_router(extraction_api.router)
app.include_router(monitor_api.router)
app.include_router(posts_api.router)
app.include_router(sessions_api.router)
app.include_router(upload_api.router)

@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)

    if response.status_code == 200:
        logger.success(f"Request: {request.method} {request.url} {response.status_code}")
    elif response.status_code == 400:
        logger.warning(f"Request: {request.method} {request.url} {response.status_code}")
    elif response.status_code == 500:
        logger.error(f"Request: {request.method} {request.url} {response.status_code}")
    else:
        logger.info(f"Request: {request.method} {request.url} {response.status_code}")

    return response

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=int(PORT), log_level="debug")