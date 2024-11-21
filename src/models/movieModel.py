#!/usr/bin/env python3
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    genre: str = Field(...)
    duration: int = Field(...)
    description: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
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
        schema_extra = {
            "example": {
                "title": "Inception",
                "genre": "Sci-Fi",
                "duration": 148,
                "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
            }
        }
