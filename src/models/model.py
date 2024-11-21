#modelo para movie listo
#!/usr/bin/env python3
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    movie_id: int = Field(...)
    title: str = Field(...)
    genre: str = Field(...)
    duration: int = Field(..., description="Duration in minutes")
    description: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "8d82c2b1-9c62-47c8-bc3a-9e2c3ef7eccc",
                "movie_id": 1,
                "title": "Inception",
                "genre": "Sci-Fi",
                "duration": 148,
                "description": (
                    "A thief who steals corporate secrets through the use of "
                    "dream-sharing technology is given the inverse task of "
                    "planting an idea into the mind of a C.E.O."
                )
            }
        }


class MovieUpdate(BaseModel):
    movie_id: Optional[int]
    title: Optional[str]
    genre: Optional[str]
    duration: Optional[int]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Interstellar",
                "genre": "Sci-Fi",
                "duration": 169,
                "description": (
                    "A team of explorers travel through a wormhole in space "
                    "in an attempt to ensure humanity's survival."
                )
            }
        }
