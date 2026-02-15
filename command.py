import os

class CommandHandler:
    def __init__(self):
        self.commands = {
            "help": self.help,
            "exit": self.exit,
            "clear": self.clear,
            "pwd": self.pwd,
            "ls": self.ls,
        }

    def handle(self, command_input):
        parts = command_input.split()
        command = parts[0].lower()

        if command in self.commands:
            return self.commands[command]()
        else:
            print("Command Not Found! Type 'help' to see available commands.")
            return True

    def help(self):
        print("""
            Available Commands:
            help - Show Available Commands,
            exit - Exit celestia,
            clear - clear celstia,
            pwd - show current directory,
            ls - List Files in the current directory
            """)  
        return True

    def exit(self):
        print("Goodbye!")
        return False

    def clear(self):
        os.system("clear")
        return True

    def pwd(self):
        print(os.getcwd())
        return True

    def ls(self):
        files = os.listdir()
        for file in files:
            print(file)
        return True     