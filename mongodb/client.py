#!/usr/bin/env python3
import argparse
import logging
import os
import requests
import json

# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('client.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# Read env vars related to API connection
API_URL = os.getenv("API_URL", "http://localhost:8000")

def print_item(item):
    for k, v in item.items():
        print(f"{k}: {v}")
    print("=" * 50)

def list_items(item_type, genre=None):
    suffix = f"/{item_type}"
    endpoint = API_URL + suffix
    params = {"genre": genre} if genre else {}
    response = requests.get(endpoint, params=params)
    if response.ok:
        json_resp = response.json()
        for item in json_resp:
            print_item(item)
    else:
        print(f"Error: {response}")

def get_item_by_id(item_type, id):
    suffix = f"/{item_type}/{id}"
    endpoint = API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        print_item(json_resp)
    else:
        print(f"Error: {response}")

def update_item(item_type, id):
    suffix = f"/{item_type}/{id}"
    endpoint = API_URL + suffix
    # Example payload for update
    data = {
        "title": "Updated Title" if item_type == "movie" else None,
        "username": "updated_user" if item_type == "user" else None,
        "name": "Updated Theater" if item_type == "theater" else None,
        "showtime": "2025-01-01T00:00:00" if item_type == "showtime" else None,
        "status": "read" if item_type == "notification" else None
    }
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.put(endpoint, json=data)
    if response.ok:
        print(f"{item_type.capitalize()} with ID {id} has been updated successfully.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def delete_item(item_type, id):
    suffix = f"/{item_type}/{id}"
    endpoint = API_URL + suffix
    response = requests.delete(endpoint)
    if response.ok:
        print(f"{item_type.capitalize()} with ID {id} has been deleted successfully.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    log.info(f"Welcome to the catalog client. App requests to: {API_URL}")

    parser = argparse.ArgumentParser()

    list_of_actions = ["search", "get", "update", "delete"]
    list_of_item_types = ["movie", "showtime", "theater", "user", "notification"]
    parser.add_argument("action", choices=list_of_actions,
                        help="Action to be used for the library")
    parser.add_argument("item_type", choices=list_of_item_types,
                        help="Type of item to perform the action on")
    parser.add_argument("-i", "--id",
                        help="Provide an item ID which is related to the action", default=None)
    parser.add_argument("-g", "--genre",
                        help="Search parameter to look for items with a specific genre", default=None)

    args = parser.parse_args()

    if args.id and args.action not in ["get", "update", "delete"]:
        log.error(f"Can't use arg id with action {args.action}")
        exit(1)

    if args.genre and args.action != "search":
        log.error(f"Genre arg can only be used with search action")
        exit(1)

    if args.action == "search":
        list_items(args.item_type, args.genre)
    elif args.action == "get" and args.id:
        get_item_by_id(args.item_type, args.id)
    elif args.action == "update" and args.id:
        update_item(args.item_type, args.id)
    elif args.action == "delete" and args.id:
        delete_item(args.item_type, args.id)

if __name__ == "__main__":
    main()
