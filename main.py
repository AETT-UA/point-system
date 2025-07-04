
from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sys

#routers
from routes import basic_router

#logging handlers
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="ERROR")
logger.add(sys.stdout, format="{time} {level} {message}", filter="my_module", level="DEBUG")
logger.add(sys.stdout, format="{time} {level} {message}", filter="my_module", level="INFO")

app = FastAPI()

# routers
app.include_router(basic_router.router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    logger.info("Application up and running!")
    return {"Up and running"} 
