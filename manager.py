import json
class manager:
    def __init__(self):
        self.filename = "none"
    def load(self,filename):
        self.filename = filename
        try:
            with open(self.filename,"r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("file not found.")
            return False
        except json.JSONDecodeError:
            print("file is not a valid json file.")
            return False
        return True
    def read(self,key):
        if(key not in self.data):
            return "key not found"
        return self.data[key]
    def write(self, key, value):
        self.data[key] = value
        self.save()
        
    def save(self):
        with open(self.filename,"w") as f:
            json.dump(self.data,f)