import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, "App", "config", ".env"))

app = FastAPI()

HOST = os.getenv("HOST","127.0.0.1")
PORT = os.getenv("PORT","8000")

@app.get("/")
def read_root():
    print(os.getenv("HOST"))
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=int(PORT), log_level="debug")