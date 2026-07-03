import json
import sys
print("Welcome to the python json inspecter. This is a program that will allow you to inspect a json file and easally navagate threw it.")
filename = input("Please enter the name of the json file you would like to inspect.")
with open(filename,"r") as f:
    data = json.load(f)
print("json loaded")
