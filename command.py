import os

class CommandHandler:
    def __init__(self):
        self.commands = {
            "help": self.help,
            "exit": self.exit,
            "clear": self.clear,
            "pwd": self.pwd,
            "ls": self.ls,
            "echo": self.echo,
        }

    def handle(self, command_input):
        parts = command_input.split()
        command = parts[0].lower()
        args = parts[1:]

        if command in self.commands:
            return self.commands[command](args)
        else:
            print("Command Not Found! Type 'help' to see available commands.")
            return True

    def help(self, args):
        print("""
            Available Commands:
            help - Show Available Commands,
            exit - Exit celestia,
            clear - clear celstia,
            pwd - show current directory,
            ls - List Files in the current directory
            """)  
        return True

    def exit(self, args):
        print("Goodbye!")
        return False

    def clear(self, args):
        os.system("clear")
        return True

    def pwd(self, args):
        print(os.getcwd())
        return True

    def ls(self, args):
        files = os.listdir()
        for file in files:
            print(file)
        return True    

    def echo(self, args):
        if not args:
            print("Usage: echo <message>")
        else:
            print(" ".join(args))
        return True         