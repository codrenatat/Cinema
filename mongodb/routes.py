#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from model import Movie, MovieUpdate, Showtime, Theater, User

movie_router = APIRouter()
showtime_router = APIRouter()
theater_router = APIRouter()
user_router = APIRouter()

# Rutas para Movie
@movie_router.post("/", response_description="Post a new movie", status_code=status.HTTP_201_CREATED, response_model=Movie)
def create_movie(request: Request, movie: Movie = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = request.app.database["movies"].insert_one(movie)
    created_movie = request.app.database["movies"].find_one({"_id": new_movie.inserted_id})
    return created_movie

@movie_router.get("/", response_description="Get all movies", response_model=List[Movie])
def list_movies(request: Request, genre: str = ""):
    if genre:
        movies = list(request.app.database["movies"].find({"genre": genre}))
    else:
        movies = list(request.app.database["movies"].find())
    return movies

@movie_router.get("/{id}", response_description="Get a single movie by id", response_model=Movie)
def find_movie(id: str, request: Request):
    if (movie := request.app.database["movies"].find_one({"_id": id})) is not None:
        return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

@movie_router.put("/{id}", response_description="Update a movie by id", response_model=Movie)
def update_movie(id: str, request: Request, movie: MovieUpdate = Body(...)):
    updated_data = {k: v for k, v in movie.dict().items() if v is not None}
    if updated_data:
        update_result = request.app.database["movies"].update_one({"_id": id}, {"$set": updated_data})
        if update_result.modified_count == 1:
            if (updated_movie := request.app.database["movies"].find_one({"_id": id})) is not None:
                return updated_movie
    if (existing_movie := request.app.database["movies"].find_one({"_id": id})) is not None:
        return existing_movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

@movie_router.delete("/{id}", response_description="Delete a movie")
def delete_movie(id: str, request: Request, response: Response):
    delete_result = request.app.database["movies"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

# Rutas para Showtime
@showtime_router.post("/", response_description="Post a new showtime", status_code=status.HTTP_201_CREATED, response_model=Showtime)
def create_showtime(request: Request, showtime: Showtime = Body(...)):
    showtime = jsonable_encoder(showtime)
    new_showtime = request.app.database["showtimes"].insert_one(showtime)
    created_showtime = request.app.database["showtimes"].find_one({"_id": new_showtime.inserted_id})
    return created_showtime

@showtime_router.get("/", response_description="Get all showtimes", response_model=List[Showtime])
def list_showtimes(request: Request):
    showtimes = list(request.app.database["showtimes"].find())
    return showtimes

@showtime_router.get("/{id}", response_description="Get a single showtime by id", response_model=Showtime)
def find_showtime(id: str, request: Request):
    if (showtime := request.app.database["showtimes"].find_one({"_id": id})) is not None:
        return showtime
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Showtime with ID {id} not found")

@showtime_router.put("/{id}", response_description="Update a showtime by id", response_model=Showtime)
def update_showtime(id: str, request: Request, showtime: Showtime = Body(...)):
    updated_data = {k: v for k, v in showtime.dict().items() if v is not None}
    if updated_data:
        update_result = request.app.database["showtimes"].update_one({"_id": id}, {"$set": updated_data})
        if update_result.modified_count == 1:
            if (updated_showtime := request.app.database["showtimes"].find_one({"_id": id})) is not None:
                return updated_showtime
    if (existing_showtime := request.app.database["showtimes"].find_one({"_id": id})) is not None:
        return existing_showtime
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Showtime with ID {id} not found")

@showtime_router.delete("/{id}", response_description="Delete a showtime")
def delete_showtime(id: str, request: Request, response: Response):
    delete_result = request.app.database["showtimes"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Showtime with ID {id} not found")

# Rutas para Theater
@theater_router.post("/", response_description="Post a new theater", status_code=status.HTTP_201_CREATED, response_model=Theater)
def create_theater(request: Request, theater: Theater = Body(...)):
    theater = jsonable_encoder(theater)
    new_theater = request.app.database["theaters"].insert_one(theater)
    created_theater = request.app.database["theaters"].find_one({"_id": new_theater.inserted_id})
    return created_theater

@theater_router.get("/", response_description="Get all theaters", response_model=List[Theater])
def list_theaters(request: Request):
    theaters = list(request.app.database["theaters"].find())
    return theaters

@theater_router.get("/{id}", response_description="Get a single theater by id", response_model=Theater)
def find_theater(id: str, request: Request):
    if (theater := request.app.database["theaters"].find_one({"_id": id})) is not None:
        return theater
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Theater with ID {id} not found")

@theater_router.put("/{id}", response_description="Update a theater by id", response_model=Theater)
def update_theater(id: str, request: Request, theater: Theater = Body(...)):
    updated_data = {k: v for k, v in theater.dict().items() if v is not None}
    if updated_data:
        update_result = request.app.database["theaters"].update_one({"_id": id}, {"$set": updated_data})
        if update_result.modified_count == 1:
            if (updated_theater := request.app.database["theaters"].find_one({"_id": id})) is not None:
                return updated_theater
    if (existing_theater := request.app.database["theaters"].find_one({"_id": id})) is not None:
        return existing_theater
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Theater with ID {id} not found")

@theater_router.delete("/{id}", response_description="Delete a theater")
def delete_theater(id: str, request: Request, response: Response):
    delete_result = request.app.database["theaters"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Theater with ID {id} not found")

# Rutas para User
@user_router.post("/", response_description="Post a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one({"_id": new_user.inserted_id})
    return created_user

@user_router.get("/", response_description="Get all users", response_model=List[User])
def list_users(request: Request):
    users = list(request.app.database["users"].find())
    return users

@user_router.get("/{id}", response_description="Get a single user by id", response_model=User)
def find_user(id: str, request: Request):
    if (user := request.app.database["users"].find_one({"_id": id})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")

@user_router.put("/{id}", response_description="Update a user by id", response_model=User)
def update_user(id: str, request: Request, user: User = Body(...)):
    updated_data = {k: v for k, v in user.dict().items() if v is not None}
    if updated_data:
        update_result = request.app.database["users"].update_one({"_id": id}, {"$set": updated_data})
        if update_result.modified_count == 1:
            if (updated_user := request.app.database["users"].find_one({"_id": id})) is not None:
                return updated_user
    if (existing_user := request.app.database["users"].find_one({"_id": id})) is not None:
        return existing_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")

@user_router.delete("/{id}", response_description="Delete a user")
def delete_user(id: str, request: Request, response: Response):
    delete_result = request.app.database["users"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")
