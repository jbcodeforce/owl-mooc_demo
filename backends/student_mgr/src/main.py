"""
Copyright 2024 Intelligent Automations LLC
@author Jerome Boyer
"""
import os
from dotenv import load_dotenv
from app_settings import get_config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import students
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # everything before yield is done before the app starts
    load_dotenv(dotenv_path=get_config().owl_env_path)
    yield
    # do something when app stop

app = FastAPI(lifespan=lifespan)

# List of authorized origins
origins = os.getenv("OWL_CLIENTS", ["http://localhost:3000"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)

@app.get(get_config().api_route + "/health")
def alive() -> dict[str,str]:
    return {"Status": "Alive"}

@app.get(get_config().api_route + "/version")
def version():
    return {"Version": get_config().version}