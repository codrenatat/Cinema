#!/usr/bin/env python3
import csv
import json
import requests

BASE_URL = "http://localhost:8000"

def post_csv_to_api(file_path, endpoint):
    with open(file_path, mode='r') as fd:
        csv_data = csv.DictReader(fd)
        for row in csv_data:
            # Convertir campos específicos a listas o diccionarios si es necesario y si no están vacíos
            if 'preferences' in row and row['preferences'].strip():
                row['preferences'] = row['preferences'].split(',')
            if 'activity_log' in row and row['activity_log'].strip():
                try:
                    row['activity_log'] = json.loads(row['activity_log'])
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError for activity_log: {e}")
                    row['activity_log'] = []
            if 'watchlist' in row and row['watchlist'].strip():
                try:
                    row['watchlist'] = json.loads(row['watchlist'])
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError for watchlist: {e}")
                    row['watchlist'] = []
            if 'feedback' in row and row['feedback'].strip():
                try:
                    row['feedback'] = json.loads(row['feedback'])
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError for feedback: {e}")
                    row['feedback'] = []
            if 'booking_history' in row and row['booking_history'].strip():
                try:
                    row['booking_history'] = json.loads(row['booking_history'])
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError for booking_history: {e}")
                    row['booking_history'] = []
            if 'rating_reviews' in row and row['rating_reviews'].strip():
                try:
                    row['rating_reviews'] = json.loads(row['rating_reviews'])
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError for rating_reviews: {e}")
                    row['rating_reviews'] = []

            # Manejar campo de fecha desactivado
            if 'deactivated_at' in row and not row['deactivated_at'].strip():
                row['deactivated_at'] = None

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
        (r".\csv\users.csv", "user"),
        (r".\csv\notifications.csv", "notification")
    ]

    for file_path, endpoint in files_endpoints:
        post_csv_to_api(file_path, endpoint)

if __name__ == "__main__":
    main()
