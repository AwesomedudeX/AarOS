def cal():

    print(len("Calendar")*"-"+"\nCalendar\n"+"-"*len("Calendar"))
    print("\nNote: Console must be shut down for Calendar changes to be saved.\n\nLoading...\n\n")

    from datetime import datetime as dt
    import pandas as pd
    import warnings
    import os

    warnings.filterwarnings("ignore")
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    acts = {
        "actions": "Lets you view a list of possible actions.",
        "view": "Lets you view your calendar.",
        "add": "Lets you add an event to your calendar.",
        "del": "Lets you delete an event on your calendar."
    }

    m = dt.now().strftime("%B")
    cal = pd.read_csv("calendarsource.csv")
    cal.set_index("Time", inplace=True)
    dc = 0

    if m not in str(cal.columns[0]):

        for i in range(len(cal.columns)):

            if i + 1 > 9:
                cal.rename(columns={cal.columns[i]: "July" + " " + str(i + 1)}, inplace=True)
            else:
                cal.rename(columns={cal.columns[i]: "July" + " 0" + str(i + 1)}, inplace=True)

            cal[cal.columns[i]] = ["Empty Slot" for i in range(24)]

    while True:
        
        try:
        
            choice = input("\nWhat do you want to do (type \'actions\' for a list of things that you can do)? ")
    
            if choice == "q" or choice == "quit" or choice == "close" or choice == "exit" or choice == "back" or choice == "return" or choice == "exit":
                print("\nApp Closed.")
                break
    
            elif choice == "acts" or choice == "actions" or choice == "choices" or choice == "lst":
                print()
                for x, y in zip(acts.keys(), acts.values()):
                    print(f" - \'{x}\': {y}")
    
            elif choice == "view" or choice == "calendar" or choice == "cal":
    
                day = input("What day (number) do you want to view events for (type \'all\' to view all days, \'multi\' to view multiple days or \'return\' to go back)? ").lower()
    
                if day == "q" or day == "quit" or day == "close" or day == "exit" or day == "back" or day == "return" or day == "exit":
                    pass
    
                elif day == "all" or day == "everything":
                    print(cal)
    
                elif day == "mult" or day == "multi" or day == "multiple":
    
                    s = int(input("Enter the starting day for the list of days that you want to view here: "))
                    e = int(input("Enter the ending day for the list of days that you want to view here: "))
    
                    print()
    
                    for i in range(s, e+1):
    
                        if i <= 9:
    
                            print(f"\n{m} 0{i}:\n")
    
                            for x, y in zip(cal.index, cal[f"{m} 0{i}"]):
                                print(f"{x}: {y}")
    
                        else:
    
                            print(f"\n{m} {i}:\n")
    
                            for x, y in zip(cal.index, cal[f"{m} {i}"]):
                                print(f"{x}: {y}")
    
            elif choice == "add" or choice == "new" or choice == "create" or choice == "add event" or choice == "new event" or choice == "create event":
    
                day = input("What day do you want to add this event to (type \'return\' to go back)? ")
    
                if day == "q" or day == "quit" or day == "close" or day == "exit" or day == "back" or day == "return" or day == "exit":
                    pass
    
                else:
    
                    if int(day) <= 9:
                        elst = dict(cal[f"{m} 0{day}"])
                    else:
                        elst = dict(cal[f"{m} {day}"])
    
                    name = input("What would you like to name your event? ")
                    time = input("When is this event (format: \'<hour number> <AM/PM>\')? ")
                    elst[time] = name
    
                    if int(day) <= 9:
                        cal[f"{m} 0{day}"] = list(elst.values())
                    else:
                        cal[f"{m} {day}"] = list(elst.values())
    
                    print("\nEvent added successfully.\n")
    
            elif choice == "del" or choice == "delete" or choice == "remove" or choice == "delete event" or choice == "del event" or choice == "remove event":
    
                day = input("What day is this event on (type \'return\' to go back)? ")
    
                if day == "q" or day == "quit" or day == "close" or day == "exit" or day == "back" or day == "return" or day == "exit":
                    pass
    
                else:
    
                    if int(day) <= 9:
                        elst = dict(cal[f"{m} 0{day}"])
                    else:
                        elst = dict(cal[f"{m} {day}"])
    
                    time = input("What time is the event that you want to delete? (format: \'<hour number> <AM/PM>\')? ")
                    elst[time] = "Empty Slot"
    
                    if int(day) <= 9:
                        cal[f"{m} 0{day}"] = list(elst.values())
                    else:
                        cal[f"{m} {day}"] = list(elst.values())
    
                    print("\nEvent added successfully.\n")
    
            else:
                print("\nInvalid input. Please try again.\n")

        except:
            print("\nThere was an error. Please try again.\n")

    os.remove("calendarsource.csv")
    cal.to_csv("calendarsource.csv")

# cal()