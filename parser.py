import actions
commands = {"help":actions.help}
def parse(command):
    if(command in commands):
        func = commands[command]
        func()
    else:
        print("command not found. Type help for a list of commands.")
