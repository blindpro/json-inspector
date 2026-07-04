import actions
commands = {"help":actions.help,"read":actions.read,"quit":actions.quit}
def parse(command):
    if(command in commands):
        func = commands[command]
        func()
    else:
        print("command not found. Type help for a list of commands.")
def load(filename):
    actions.load(filename)