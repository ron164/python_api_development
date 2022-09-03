# -*- coding: utf-8 -*-
# @Time : 27-08-2022 10:36
# @Author : rohan
# @File : main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)

origins = ["*"]
# origins = ["https://www.google.com", "https://www.youtube.com/"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Restrict POST/DELETE request
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {'message': 'Hello welcome to my API'}