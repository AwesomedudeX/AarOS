def fm():

    print("-"*23+"\nFile Creator and Editor\n"+"-"*23)
    print("\n(Note: Shut down the console to apply changes)")

    import os

    while True:

        action = str(input("\nEnter what you want to do here (\'write\' - rewrites the file, \'read\' - lets you read the file, \'delete\' to delete a file, \'mf\' to make a folder, \'move\' to move a file or \'quit\' to quit the software): ")).lower()

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

            elif action == "del" or action == "delete" or action == "d":
                file = str(input("Enter the name of the file that you want to delete with its extension (\'.txt\', \'.py\', etc.): "))
                os.remove(file)
                print(f"{file} deleted successfully.")

            elif action == "read" or action == "r":
                name = str(input("Enter the name of the file with the extension (\'.txt\', \'.py\', etc.): "))
                file = open(name, "r")
                read = file.read()
                print(f"\n{'-'*200}\n{read}\n{'-'*200}\n")

            elif action == "move" or action == "mv":

                name = str(input("Enter the name of the file with the extension (\'.txt\', \'.py\', etc.): "))
                folder = input("What folder do you want to move this file to (type \'/q/\' to go back)? ")

                if folder != "/q/":

                    os.system(f"mv {name} {folder}\\{name}")

            elif action == "mkdir" or action == "make directory" or action == "make folder" or action == "mf" or action == "mkf" or action == "create folder" or action == "create directory":

                print("\n(Note: Folder name cannot contain any of the following characters: \'/\', \'\\\', \'?\', \':\', \'|\', \'<\', \'>\', \'*\', \'\"\'. Also, an existing folder cannot be recreated, as this will crash the app.)\n")

                name = input("What do you want to name your folder (type \'/q/\' to go back)? ")

                if name != "/q/":
                    os.mkdir(name)

            else:
                print("Invalid option. Please try again.")
