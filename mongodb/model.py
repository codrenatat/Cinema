import uuid
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

# Modelo para Movie
class Movie(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    genre: str = Field(...)
    duration: int = Field(...)
    description: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "f54a9f9c-bac9-43f4-a0fa-fffd0dc9270c",
                "title": "Inception",
                "genre": "Sci-Fi",
                "duration": 148,
                "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
            }
        }

class MovieUpdate(BaseModel):
    title: Optional[str]
    genre: Optional[str]
    duration: Optional[int]
    description: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Inception",
                "genre": "Sci-Fi",
                "duration": 148,
                "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
            }
        }

# Modelo para Showtime
class Showtime(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    movie_id: str = Field(...)
    theater_id: str = Field(...)
    showtime: datetime = Field(...)
    available_seats: int = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "e54a9f9c-bac9-43f4-a0fa-fffd0dc9270c",
                "movie_id": "f54a9f9c-bac9-43f4-a0fa-fffd0dc9270c",
                "theater_id": "5fb789c1def0e105d7cbbc20",
                "showtime": "2024-11-21T18:00:00",
                "available_seats": 150
            }
        }

# Modelo para Theater
class Theater(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    location: str = Field(...)
    seating_capacity: int = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "5fb789c1def0e105d7cbbc20",
                "name": "Cinema Center Downtown",
                "location": "New York",
                "seating_capacity": 250
            }
        }

# Modelo para User
class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    hashed_password: str = Field(...)
    created_at: datetime = Field(...)
    last_login: Optional[datetime] = Field(None)
    preferences: List[str] = Field(default_factory=list)
    activity_timestamp: Optional[datetime] = Field(None)
    activity_type: Optional[str] = Field(None)
    activity_details: Optional[str] = Field(None)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "5e12b4c9a7896d5c2f34bc72",
                "username": "jane_smith",
                "email": "jane.smith@example.com",
                "hashed_password": "$2b$12$Qb45tFD/C4G2pRZ1kR3.yzJ9z9sdghsPJ6v/xwTraDnBqLGJHvUmz",
                "created_at": "2022-09-10T12:25:00Z",
                "last_login": "2024-11-19T15:30:00Z",
                "preferences": ["Romance", "Comedy", "Drama"],
                "activity_timestamp": "2024-11-19T15:35:00Z",
                "activity_type": "login",
                "activity_details": "User logged in from IP 10.0.0.5"
            }
        }
