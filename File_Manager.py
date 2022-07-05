def fm():

    print("-"*23+"\nFile Creator and Editor\n"+"-"*23)
    print("\n(Note: Restart the console to apply changes)")

    while True:

        action = str(input("\nEnter what you want to do here (\'write\' - rewrites the file, \'add\' - lets you add more text to your file, \'read\' - lets you read the file, or \'quit\' to quit the software): ")).lower()

        if action == "q" or action == "quit" or action == "close" or action == "exit":
            print("\nApp Closed.")
            break

        else:

            if action == "write" or action == "w":

                name = str(input("Enter the name of the file with the extension (\'.txt\', \'.py\', etc.): "))

                file = open(name, "w")

                print("\n(Type \'/q/\' to exit the editor)\n\n")

                line = 1

                text = input(f"Line {line}: ")
                line += 1

                if text != "/q/":

                    write = text

                    while True:

                        if text == "/q/":
                            break

                        else:

                            text = input(f"Line {line}: ")
                            write = write+"\n"+text
                            line += 1

                    file.write(write)

                print(name, "was rewritten successfully.")

            elif action == "read" or action == "r":
                name = str(input("Enter the name of the file with the extension (\'.txt\', \'.py\', etc.): "))
                file = open(name, "r")
                read = file.read()
                print(f"\n{'-'*200}\n{read}\n{'-'*200}\n")


            else:
                print("Invalid option. Please try again.")


# fce()