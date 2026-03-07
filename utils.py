import json
import os

DATA_FILE="data/data.json"

def load_case():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,"r") as file:
        data=json.load(file)
        return data.get("cases",[])
    
def save_case(case):
    with open(DATA_FILE,"r") as file:
        data=json.load(file)
    
    data["cases"]=case

    with open(DATA_FILE,"w") as file:
        json.dump(data,file,indent=4)

