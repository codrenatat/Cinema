#!/usr/bin/env python3
import csv
import requests

BASE_URL = "http://localhost:8000"

def main():
    with open("movies.csv") as fd:
        movies_csv = csv.DictReader(fd)
        for movie in movies_csv:
            del movie["movie_id"]
            #movie["genre"] = movie["genre"].split("/")  # Assuming genres are separated by "/"
            x = requests.post(BASE_URL+"/movie", json=movie)
            if not x.ok:
                print(f"Failed to post movie {x} - {movie}")

if __name__ == "__main__":
    main()
