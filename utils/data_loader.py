# utils/data_loader.py
import json

def load_json_data(filename, key):
    with open(f"resources/test_data/{filename}", 'r') as file:
        data = json.load(file)
    return data[key]
