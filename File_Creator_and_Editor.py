def fce():

    print("-"*23+"\nFile Creator and Editor\n"+"-"*23)
    print("\n(Note: Restart the app to apply changes)")

    while True:

        action = str(input("\nEnter what you want to do here (\'write\' - rewrites the file, \'add\' - lets you add more text to your file, \'read\' - lets you read the file, or \'quit\' to quit the software): "))

        if action == "q" or action == "quit" or action == "close" or action == "exit":
            print("\nApp Closed.")
            break

        else:

            name = str(input("Enter the name of the file (use \'.txt\', \'.py\', etc. after the file name): "))

            if action == "write" or action == "w":
                text = str(input("Enter your text here: "))
                file = open(name, "w")
                file.write(text)
                print(name, "was rewritten successfully.")


            elif action == "add" or action == "a":
                text = str(input("Enter your text here: "))
                file = open(name, "a")
                file.write(text)
                print("Text added successfully to", name+".")


            elif action == "read" or action == "r":
                file = open(name, "r")
                file.read()


            else:
                print("Invalid option. Please try again.")


# fce()