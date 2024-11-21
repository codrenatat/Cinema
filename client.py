#!/usr/bin/env python3
import argparse
import logging
import os
import requests

# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('movies.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# Read env vars related to API connection
MOVIES_API_URL = os.getenv("MOVIES_API_URL", "http://localhost:8000")

def print_movie(movie):
    for k in movie.keys():
        print(f"{k}: {movie[k]}")
    print("=" * 50)

def list_movies(genre):
    suffix = "/movie"
    endpoint = MOVIES_API_URL + suffix
    params = {
        "genre": genre
    }
    response = requests.get(endpoint, params=params)
    if response.ok:
        json_resp = response.json()
        for movie in json_resp:
            print_movie(movie)
    else:
        print(f"Error: {response}")

def get_movie_by_id(id):
    suffix = f"/movie/{id}"
    endpoint = MOVIES_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        print_movie(json_resp)
    else:
        print(f"Error: {response}")

def update_movie(id):
    pass

def delete_movie(id):
    pass

def main():
    log.info(f"Welcome to movies catalog. App requests to: {MOVIES_API_URL}")

    parser = argparse.ArgumentParser()

    list_of_actions = ["search", "get", "update", "delete"]
    parser.add_argument("action", choices=list_of_actions,
                        help="Action to be used for the movies library")
    parser.add_argument("-i", "--id",
                        help="Provide a movie ID which is related to the movie action", default=None)
    parser.add_argument("-g", "--genre",
                        help="Search parameter to look for movies with a specific genre", default=None)

    args = parser.parse_args()

    if args.id and args.action not in ["get", "update", "delete"]:
        log.error(f"Can't use arg id with action {args.action}")
        exit(1)

    if args.genre and args.action != "search":
        log.error(f"Genre arg can only be used with search action")
        exit(1)

    if args.action == "search":
        list_movies(args.genre)
    elif args.action == "get" and args.id:
        get_movie_by_id(args.id)
    elif args.action == "update":
        update_movie(args.id)
    elif args.action == "delete":
        delete_movie(args.id)

if __name__ == "__main__":
    main()
