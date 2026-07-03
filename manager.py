import json
class manager:
    def __init__(self,filename):
        self.filename = filename
        self.load()
    def load(self):
        with open(self.filename,"r") as f:
            self.data = json.load(f)
    