#!/usr/bin/env python3
import csv
import requests

BASE_URL = "http://localhost:8000"

def post_csv_to_api(file_path, endpoint):
    with open(file_path, mode='r') as fd:
        csv_data = csv.DictReader(fd)
        for row in csv_data:
            if 'preferences' in row:
                row['preferences'] = row['preferences'].split(',')
            
            response = requests.post(f"{BASE_URL}/{endpoint}", json=row)
            if not response.ok:
                print(f"Failed to post to {endpoint}: {response.status_code} - {response.text}")
            else:
                print(f"Successfully posted to {endpoint}: {row}")

def main():
    files_endpoints = [
        (r".\csv\movies.csv", "movie"),
        (r".\csv\showtime.csv", "showtime"),
        (r".\csv\theater.csv", "theater"),
        (r".\csv\users.csv", "user")
    ]

    for file_path, endpoint in files_endpoints:
        post_csv_to_api(file_path, endpoint)

if __name__ == "__main__":
    main()
