import manager
import sys
print("Welcome to the python json inspecter. This is a program that will allow you to inspect a json file and easally navagate threw it.")
filename = input("Please enter the name of the json file you would like to inspect.")
data = manager.load(filename)
print("json loaded")
