# utils/database.py

import json
import os

DB_PATH = "data/mapping.json"

def load_data():
    if not os.path.exists(DB_PATH):
        save_data({})
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_mapping(user_id, message_id):
    data = load_data()
    data[str(user_id)] = message_id
    save_data(data)

def get_mapping(user_id):
    data = load_data()
    return data.get(str(user_id))