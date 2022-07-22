def fit():

    print("-"*len("AarOS Fitness")+"\nAarOS Fitness\n"+"-"*len("AarOS Fitness"))
    print("\nNote: You can update your information in the Settings app.\n\nLoading...\n\n")

    import settingsource as ss
    import fitsource as src

    exercises = src.exercises

    acts = {
        "info": "Lets you view your fitness-related information",
        "new": "Lets you log a new exercise",
        "view": "Lets you view your exercises",
        "quit": "Closes the app"
    }
    info = {
        "Age": ss.age,
        "Sex": ss.sex,
        "Maximum Heart Rate": str(ss.maxhr) + "BPM",
        "Weight": None,
        "Height": None,
        "BMI": None,
        "Average Calories Burnt Per Day": None
    }

    if ss.weight != None:
        info["Weight"] = str(ss.weight) + "kg"
    else:
        info["Weight"] = "N/A"

    if ss.height != None:
        info["Height"] = str(ss.height) + "cm"
    else:
        info["Height"] = "N/A"

    if info["Height"] != "N/A" and info["Weight"] != "N/A":
        info["BMI"] = round(float(info["Weight"][:-2]) / (float(info["Height"][:-2])/100) ** 2)
    else:
        info["BMI"] = "N/A"

    if info["Sex"] == 1 and info["Height"] != "N/A" and info["Weight"] != "N/A" and info["Age"] != None:
        info["Average Calories Burnt Per Day"] = str(round(66 + (6.2 * ss.weight) + (12.7 * ss.height) - (6.76 * ss.age)))
        info["Sex"] = "Male"
    elif info["Sex"] == 0 and info["Height"] != "N/A" and info["Weight"] != "N/A" and info["Age"] != None:
        info["Average Calories Burnt Per Day"] = str(round(655.1 + (4.35 * ss.weight) + (4.7 * ss.height) - (4.7 * ss.age)))
        info["Sex"] = "Male"
    else:
        info["Average Calories Burnt Per Day"] = "N/A"
        info["Sex"] = "N/A"

    while True:

        choice = input("\nWhat do you want to do (type \'actions\' to list things that you can do or type \'quit\' to quit)? ").lower()

        if choice == "q" or choice == "quit" or choice == "close" or choice == "exit" or choice == "back" or choice == "return" or choice == "exit":
            print("\nApp Closed.")
            break

        else:

                if choice == "acts" or choice == "actions" or choice == "choices" or choice == "lst":
                    print()
                    for x, y in zip(acts.keys(), acts.values()):
                        print(f" - {x}: {y}.")

                elif choice == "info" or choice == "my info" or choice == "information" or choice == "my information":
                    print()
                    for x, y in zip(info.keys(), info.values()):
                        print(f"{x}: {y}")

                elif choice == "log" or choice == "log exercise" or choice == "add exercise" or choice == "new exercise" or choice == "new" or choice == "add":

                    exercise = input("\nWhat exercise did you do (type \'return\' to go back)? ")

                    if exercise != "return" and exercise != "back" and exercise != "quit" and exercise != "q" and exercise != "menu":
                        duration = int(input("How long did you do it (minutes)? "))
                        met = float(input("What is the MET Score for this exercise? "))
                        month = int(input("What month (number) did you do this exercise? "))
                        day = int(input("What day (number) did you do this exercise? "))
                        year = int(input("What year did you do this exercise? "))
                        time = input("What was the time that day when you did this exercise? ")
                        exercises.append([exercise, month, day, year, time, duration, round(0.0175*met*float(info["Weight"][:-2])*duration)])

                elif choice == "list" or choice == "view" or choice == "exercises" or choice == "view exercises":

                    year = input("What year do you want to search for (type \'return\' to go back)? ")

                    if year != "return" and year != "back" and year != "quit" and year != "q" and year != "menu":

                        year = int(year)
                        month = input("What month (number) do you want to search for (type \'all\' for all months)? ")
                        day = input("What day (number) do you want to search for (type \'all\' for all days)? ")

                        for x in exercises:
                            if year == x[3]:
                                if month != "all" and month != "everything":
                                    month = int(month)

                                    if month == x[1]:

                                        if day != "all" and day != "everything":
                                            day = int(day)

                                            if day == x[2]:
                                                print("\n\n" + "-" * len(x[0]) + f"\n{x[0]}\n" + "-" * len(x[0]) + "\n")
                                                print(f"Date: {x[1]}/{x[2]}/{x[3]}")
                                                print(f"Time: {x[4]}")
                                                print(f"Duration: {x[5]} minutes")
                                                print(f"Calories Burnt: {x[6]}")
                                        else:
                                            print("\n\n" + "-" * len(x[0]) + f"\n{x[0]}\n" + "-" * len(x[0]) + "\n")
                                            print(f"Date: {x[1]}/{x[2]}/{x[3]}")
                                            print(f"Time: {x[4]}")
                                            print(f"Duration: {x[5]} minutes")
                                            print(f"Calories Burnt: {x[6]}")

                                else:
                                    if day != "all" and day != "everything":
                                        day = int(day)

                                        if day == x[2]:
                                            print("\n\n" + "-" * len(src.exercises[int(enum) - 1][0]) + f"\n{src.exercises[int(enum) - 1][0]}\n" + "-" * len(src.exercises[int(enum) - 1][0]) + "\n")
                                            print(f"Date: {exercises[int(enum) - 1][1]}/{exercises[int(enum) - 1][2]}/{exercises[int(enum) - 1][3]}")
                                            print(f"Time: {exercises[int(enum) - 1][4]}")
                                            print(f"Duration: {exercises[int(enum) - 1][5]} minutes")
                                            print(f"Calories Burnt: {exercises[int(enum) - 1][6]}")

                                    else:
                                        print("\n\n" + "-" * len(src.exercises[int(enum) - 1][0]) + f"\n{src.exercises[int(enum) - 1][0]}\n" + "-" * len(src.exercises[int(enum) - 1][0]) + "\n")
                                        print(f"Date: {exercises[int(enum) - 1][1]}/{exercises[int(enum) - 1][2]}/{exercises[int(enum) - 1][3]}")
                                        print(f"Time: {exercises[int(enum) - 1][4]}")
                                        print(f"Duration: {exercises[int(enum) - 1][5]} minutes")
                                        print(f"Calories Burnt: {exercises[int(enum) - 1][6]}")


                else:
                    print("Invalid choice. Please try again.\n")

    write = f"exercises = {exercises}"

    source = open("fitsource.py", "w")
    source.write(write)