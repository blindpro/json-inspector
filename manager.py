import json
class manager:
    def __init__(self):
        self.filename = "none"
    def load(self,filename):
        self.filename = filename
        with open(self.filename,"r") as f:
            self.data = json.load(f)
    def read(self,key):
        if(key not in self.data):
            return "key not found"
        return self.data[key]
    