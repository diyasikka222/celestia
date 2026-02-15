def main():
    print("Welcome to Celestia")

    while True:
        try:
            command = input("Celestia > ").strip()

            if command == "":
                continue

            if command == "exit":
                print("GoodBye!")
                break
            
            print(f"You entered: {command}")

        except KeyboardInterrupt:
            print("\nExiting celestia...")
            break

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()           