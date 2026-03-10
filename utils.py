import json
import os

DATA_FILE="data/data.json"

def load_data(section):
    with open(DATA_FILE,"r") as file:
        data=json.load(file)
        return data.get(section,[])

def save_data(section,datas):
    with open(DATA_FILE,"r")as file:
        data=json.load(file)


    if section not in data:
        data[section] = []

    data[section].append(datas)
    with open(DATA_FILE,"w")as file:
        json.dump(data,file,indent=4)
