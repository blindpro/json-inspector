import parser
from json import JSONDecodeError
print("Welcome to the python json inspecter. This is a program that will allow you to inspect a json file and easally navagate threw it.")
filename = input("Please enter the name of the json file you would like to inspect.")
try:
 parser.load(filename)
except FileNotFoundError:
    print("file not found.")
    parser.parse("quit")
except JSONDecodeError:
   print("file is not a valid json file.")
   parser.parse("quit")
print("json loaded")
running = True
while(running):
    print("Please enter a command. Type help for a list of commands.")
    command = input()
    parser.parse(command)