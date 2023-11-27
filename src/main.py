from typing import Union
from fastapi import FastAPI

from .endpoints import *

app = FastAPI()

@app.get("/")
async def root():
    return ""



app.include_router(userRouter)
app.include_router(projectRouter)