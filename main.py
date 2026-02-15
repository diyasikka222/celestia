from command import CommandHandler

def main():
    print("Welcome to Celestia")
    print("Type 'help' to see available commands.")

    handler = CommandHandler()

    while True:
        try:
            command = input("Celestia > ").strip()

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