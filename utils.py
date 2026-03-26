import json
import os

DATA_FILE = "data/data.json"

def ensure_file():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"officers": [], "cases": []}, f, indent=4)

def load_data(section):
    ensure_file()
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return data.get(section, [])

    except json.JSONDecodeError:

        with open(DATA_FILE, "w") as file:
            json.dump({"officers": [], "cases": []}, file, indent=4)

        return []

    except Exception as e:
        print(f"Load error: {e}")
        return []

def save_data(section, new_entry):
    ensure_file()
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        if section not in data:
            data[section] = []

        data[section].append(new_entry)

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Save error: {e}")

def update_data(section, updated_list):
    ensure_file()
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        data[section] = updated_list

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Update error: {e}")