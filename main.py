from command import CommandHandler
import os
from rich.console import Console

console = Console()

def main():
    # print("Welcome to Celestia")
    # print("Type 'help' to see available commands.")
    console.print("[bold cyan]Welcome to Celestia[/bold cyan]")
    console.print("[dim]Type 'help' to see available commands.[/dim]")


    handler = CommandHandler()

    while True:
        try:
            # command = input("Celestia > ").strip()
            current_dir = os.path.basename(os.getcwd())
            # command = input(f"Celestia [{current_dir}] >").strip()
            console.print("[bold magenta]Celestia[/bold magenta] ", end="")
            console.print(f"[green]{current_dir}[/green] > ", end="")
            command = input().strip()

            if not command:
                continue

            should_continue = handler.handle(command)

            if not should_continue:
                break

            # if command == "exit":
            #     print("GoodBye!")
            #     break
            
            # print(f"You entered: {command}")

        except KeyboardInterrupt:
            print("\nExiting celestia...")
            break

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()           