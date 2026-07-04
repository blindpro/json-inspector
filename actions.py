from manager import manager
m = manager()
def load(filename):
    m.load(filename)
def help():
    print("commands")
    print("help. displays this message")
def read():
    key = input("Please enter the key you would like to read.")
    print(m.read(key))
    