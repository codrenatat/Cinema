#!/usr/bin/env python3
import os
from fastapi import FastAPI
from pymongo import MongoClient
from routes import user_router, movie_router, showtime_router, theater_router, notification_router

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
DB_NAME = os.getenv('MONGODB_DB_NAME', 'pro')

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(MONGODB_URI)
    app.database = app.mongodb_client[DB_NAME]
    print(f"Connected to MongoDB at: {MONGODB_URI} \n\t Database: {DB_NAME}")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Bye bye...!!")

app.include_router(user_router, tags=["users"], prefix="/user")
app.include_router(movie_router, tags=["movies"], prefix="/movie")
app.include_router(showtime_router, tags=["showtimes"], prefix="/showtime")
app.include_router(theater_router, tags=["theaters"], prefix="/theater")
app.include_router(notification_router, tags=["notifications"], prefix="/notification")


