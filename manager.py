import json
def load(filename):
    with open(filename,"r") as f:
        return json.load(f)