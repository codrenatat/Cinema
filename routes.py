#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from src.models.movieModel import Movie, MovieUpdate

router = APIRouter()

@router.post("/", response_description="Post a new movie", status_code=status.HTTP_201_CREATED, response_model=Movie)
def create_movie(request: Request, movie: Movie = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = request.app.database["movies"].insert_one(movie)
    created_movie = request.app.database["movies"].find_one(
        {"_id": new_movie.inserted_id}
    )

    return created_movie

@router.get("/", response_description="Get all movies", response_model=List[Movie])
def list_movies(request: Request, genre: str = ""):
    if genre:
        movies = list(request.app.database["movies"].find({"genre": genre}))
    else:
        movies = list(request.app.database["movies"].find())
    return movies

@router.get("/{id}", response_description="Get a single movie by id", response_model=Movie)
def find_movie(id: str, request: Request):
    if (movie := request.app.database["movies"].find_one({"_id": id})) is not None:
        return movie

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

@router.put("/{id}", response_description="Update a movie by id", response_model=Movie)
def update_movie(id: str, request: Request, movie: MovieUpdate = Body(...)):
    updated_data = {k: v for k, v in movie.dict().items() if v is not None}
    if updated_data:
        update_result = request.app.database["movies"].update_one(
            {"_id": id}, {"$set": updated_data}
        )
        if update_result.modified_count == 1:
            if (
                updated_movie := request.app.database["movies"].find_one({"_id": id})
            ) is not None:
                return updated_movie

    if (existing_movie := request.app.database["movies"].find_one({"_id": id})) is not None:
        return existing_movie

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

@router.delete("/{id}", response_description="Delete a movie")
def delete_movie(id: str, request: Request, response: Response):
    delete_result = request.app.database["movies"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")
