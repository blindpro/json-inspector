import sys
from manager import manager
m = manager()
def load(filename):
    m.load(filename)
def help():
    print("commands")
    print("help. displays this message")
    print("read. Reads a key from the .json file.")
def quit():
        print("quitting...")
        sys.exit()
def read():
    key = input("Please enter the key you would like to read.")
    print(m.read(key))
def write():
    key = input("Please enter  the key you would like to write.")
    value = input("Please enter the value you want this key to have.")
    m.write(key,value)
    print("key "+key+" written with value "+value)
