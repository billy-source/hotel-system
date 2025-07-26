# utils.py
import json
import os

ROOMS_FILE = "rooms.json"
BOOKINGS_FILE = "bookings.json"

def load_data(file, default):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump(default, f)
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def load_rooms():
    return load_data(ROOMS_FILE, [])

def save_rooms(data):
    save_data(ROOMS_FILE, data)

def load_bookings():
    return load_data(BOOKINGS_FILE, [])

def save_bookings(data):
    save_data(BOOKINGS_FILE, data)
