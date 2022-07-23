def cl():

    print("\n\n"+"-"*9+"\nChecklist\n"+"-"*9+"\n")
    print("Note: Console must be shut down for Checklist changes to be saved.")
    print("\nLoading...\n")

    import checklistsource as cls
    import os

    checklist = cls.cl

    def edit():

        item = int(input("Enter the number of the item you want to edit (or type \'return\' to go back): "))

        if item != "return" and item != "back":
            modify = input("What do you want to change the item to? ")
            checklist[item-1] = modify
            print("Item modified successfully.")

    actions = [
        "Quit the app: \'quit\'",
        "View possible actions: \'actions\'",
        "List items in checklist: \'list\'",
        "Add an item to the checklist: \'add\'",
        "Change an item in the checklist: \'edit\'",
        "Delete an item in the checklist: \'delete\'",
        "Clear the checklist: \'clear\'"
    ]

    while True:
    
        try:
    
            action = input("\nWhat do you want to do (type \'actions\' for a list of things you can do)? ")
    
            if action == "q" or action == "quit" or action == "close" or action == "exit":
                print("\nApp Closed.")
                break
    
            elif action == "actions" or action == "options" or action == "acts" or action == "opts":
                print()
                for i in actions:
                    print(" - ", i)
    
            elif action == "list" or action == "view":
                print()
                for i in range(len(checklist)):
                    print(str(i+1)+". ", checklist[i])
    
            elif action == "add" or action == "new" or action == "create":
                add = input("What are you adding to your checklist? ")
                checklist.append(add)
                print("Item added successfully.")
    
            elif action == "change" or action == "edit" or action == "modify":
                edit()
    
            elif action == "del" or action == "delete" or action == "remove":
                delete = int(input("\nEnter the number for the item that you want to delete: "))
                if delete <= len(checklist):
                    checklist.pop(delete-1)
                    print("Item", delete, "deleted successfully.")
                else:
                    print("There is no item", delete, "in your checklist.")
    
    
            elif action == "reset" or action == "clear":
    
                reset = input("Are you sure (y/n)? ")
    
                if reset == "y" or reset == "Y" or reset == "Yes" or reset == "yes":
                    checklist = []
                    print("Checklist was cleared successfully.")
                elif reset == "No" or reset == "no" or reset == "n" or reset == "N":
                    print()
                else:
                    print("Invalid input.")
    
            else:
                print("Invalid input. Please try again.\n")
        
        except:
            print("There was an error. Please try again.")
    
    try:
        source = open("checklistsource.py", "w")
        source.write("cl = [")
    
        source = open("checklistsource.py", "a")
    
        for i in range(len(checklist)-1):
            source.write("\""+checklist[i]+"\""+", ")
    
        if len(checklist) > 0:
            source.write("\"" + checklist[len(checklist) - 1] + "\"" + "]")
        else:
            source.write("]")

    except:
        print("There was an error saving the checklist.")
