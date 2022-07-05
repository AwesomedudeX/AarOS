dtf = "%B, %d %Y"
tf = "%I:%M:%S %p"

user = None
pw = None
name = None

hcl = None

def settings():

    import settingsource as src

    global dtf, tf
    global user, pw, name
    global hcl

    print("\n" + "-" * len("AarOS Settings") + "\nAarOS Settings\n" + "-" * len("AarOS Settings"))
    print("Note: Console must be restarted for changes to take effect.\n")

    if src.dtf != "":
        dtf = src.dtf
    else:
        dtf = "%B, %d %Y"

    if src.tf != "":
        tf = src.tf
    else:
        tf = "%I:%M:%S %p"

    user = src.username
    pw = src.password
    name = src.name

    hcl = src.hcl

    def dt():

        global dtf
        global tf

        while True:

            mfts = ["\'short\' - Shortened version of the month name", "\'full\' - Full month name", "\'num\' - Month number"]
            dt = input("\nWould you like to change settings for date or time (\'date\' for date, \'time\' for time or \'back\' to go back)? ").lower()

            if dt == "return" or dt == "r" or dt == "back" or dt == "b" or dt == "exit" or dt == "close" or dt == "q" or dt == "quit":
                break

            elif dt == "date" or dt == "dt" or dt == "d":

                dtf = ""

                while True:

                    e1 = input("What element do you want to appear first (Month, Day or Year)? ").lower()

                    if e1 == "month" or e1 == "m":

                        while True:

                            mf = input("\nWhat month format do you want to use (type \'formats\' for a list of month formats that you can use)? ").lower()

                            if mf == "formats" or mf == "fts":
                                print()
                                for i in mfts:
                                    print(" - "+i)

                            if mf == "short" or mf == "s" or mf == "shortened":
                                e1 = "%b"
                                break

                            elif mf == "long" or mf == "l" or mf == "full" or mf == "f":
                                e1 = "%B"
                                break

                            elif mf == "num" or mf == "numerical" or mf == "number":
                                e1 = "%m"
                                break

                        break

                    elif e1 == "day" or e1 == "d":
                        e1 = "%d"
                        break

                    elif e1 == "year" or e1 == "y":
                        e1 = "%Y"
                        break

                    else:
                        print("Invalid input. Please try again.")

                while True:

                    e2 = input("What element do you want to appear second (Month, Day or Year)? ").lower()

                    if e2 == "month" or e2 == "m":

                        while True:

                            mf = input("\nWhat month format do you want to use (type \'formats\' for a list of month formats that you can use)? ").lower()

                            if mf == "formats" or mf == "fts":
                                print()
                                for i in mfts:
                                    print(" - " + i)

                            if mf == "short" or mf == "s" or mf == "shortened":
                                e2 = "%b"
                                break

                            elif mf == "long" or mf == "l" or mf == "full" or mf == "f":
                                e2 = "%B"
                                break

                            elif mf == "num" or mf == "numerical" or mf == "number":
                                e2 = "%m"
                                break

                        break

                    elif e2 == "day" or e2 == "d":
                        e2 = "%d"
                        break

                    elif e2 == "year" or e2 == "y":
                        e2 = e2 + "%Y"
                        break

                    else:
                        print("Invalid format. Please try again.")
                        f = input("What order of elements do you want to use (separate using a \'/\' eg. MM/DD/YYYY)? ").upper()

                while True:

                    e3 = input("What element do you want to appear last (Month, Day or Year)? ").lower()

                    if e3 == "month" or e3 == "m":

                        while True:

                            mf = input("\nWhat month format do you want to use (type \'formats\' for a list of month formats that you can use)? ").lower()

                            if mf == "formats" or mf == "fts":
                                print()
                                for i in mfts:
                                    print(" - " + i)

                            if mf == "short" or mf == "s" or mf == "shortened":
                                e3 = "%b"
                                break

                            elif mf == "long" or mf == "l" or mf == "full" or mf == "f":
                                e3 = "%B"
                                break

                            elif mf == "num" or mf == "numerical" or mf == "number":
                                e3 = "%m"
                                break

                        break

                    elif e3 == "day" or e3 == "d":
                        e3 = "%d"
                        break

                    elif e3 == "year" or e3 == "y":
                        e3 = "%Y"
                        break

                    else:
                        print("Invalid format. Please try again.")


                while True:

                    s = input("What separator do you want to use for the date (\',\' or \'/\')? ")

                    if s == ",":
                        dtf = e1+", "+e2+" "+e3
                        break

                    elif s == "/":
                        dtf = e1+"/"+e2+"/"+e3
                        break

                    else:
                        print("Invalid separator. Please try again.")

            elif dt == "time" or dt == "t":

                tf = ""

                while True:

                    f = input("Do you want to use 24H or 12H time format? ").upper()

                    if f == "12H" or f == "12 HOUR" or f == "12HR" or f == "12 HR":
                        tf = tf+"%I:%M"
                        break

                    elif f == "24H" or f == "24 HOUR" or f == "24HR" or f == "24 HR":
                        tf = tf+"%H:%M"
                        break

                    else:
                        print("Invalid format. Please try again.")

                while True:

                    s = input("Seconds (On/Off): ").lower()

                    if s == "on" or s == "true" or s == "yes" or s == "y":

                        tf = tf+":%S"

                        while True:

                            ms = input("Milliseconds (On/Off): ").lower()

                            if ms == "on" or ms == "true" or ms == "yes" or ms == "y":
                                tf = tf + ".%f"
                                break
                            elif ms == "off" or ms == "false" or ms == "no" or ms == "n":
                                break
                            else:
                                print("Invalid choice. Please try again.\n")

                        break

                    elif s == "off" or s == "false" or s == "no" or s == "n":
                        break
                    else:
                        print("Invalid choice. Please try again.\n")

                while True:

                    h = input("AM/PM (On/Off): ").lower()

                    if h == "on" or h == "true" or h == "yes" or h == "y":
                        tf = tf + " %p"
                        break
                    elif h == "off" or h == "false" or h == "no" or h == "n":
                        break
                    else:
                        print("Invalid choice. Please try again.\n")



            else:
                print("Invalid input. Please try again.\n")

    def mi():

        global user
        global pw
        global name

        while True:

            userlogin = input("\nEnter your login info to continue (Don't enter anything if you haven't set your login info yet):\nUsername (Enter \'back\' to return to the settings menu): ")
            pwlogin = input("Password: ")

            if userlogin == src.username and pwlogin == src.password:

                print("Login successful.")

                name = input("\nWhat is your name? ")
                user = input("What is your new username? ")
                pw = input("What is your new password? ")

                print("\nInformation modified successfully.\n")

                break

            elif userlogin == "q" or userlogin == "quit" or userlogin == "exit" or userlogin == "close" or userlogin == "return" or userlogin == "back":
                break

            else:
                print("Invalid login info. Please try again.\n")

    def appsettings():

        global hcl

        applist = [
            "Checklist (cl)"
        ]

        while True:

            app = input("\nWhich app do you want to change settings for (type \'list\' to list modifiable apps or \'back\' to go back)? ").lower()

            if app == "q" or app == "quit" or app == "close" or app == "exit" or app == "back" or app == "return":
                break

            elif app == "list" or app == "lst" or app == "l":
                print()
                for i in applist:
                    print(" -", i)

            elif app == "checklist" or app == "cl":

                while True:

                    home = input("Do you want your checklist to be shown on your homepage? ").lower()

                    if home == "yes" or home == "y" or home == "yea" or home == "ye" or home == "ya" or home == "yeah" or home == "yeh" or home == "yah":
                        hcl = True
                        break
                    elif home == "no" or home == "n" or home == "nay" or home == "nah" or home == "na":
                        hcl = False
                        break
                    else:
                        print("Invalid choice. Please try again.\n")

            else:
                print("Invalid selection. Please try again.\n")


    settings = [
        "Date and Time (dt)",
        "My Info (mi)",
        "App Settings (as)"
    ]

    while True:

        choice = input("\nWhat setting do you want to change (type \'settings\' for a list of settings you can change or \'quit\' to close the app)? ").lower()

        if choice == "return" or choice == "r" or choice == "back" or choice == "b" or choice == "exit" or choice == "close" or choice == "q" or choice == "quit":
            print("\nApp Closed.")
            break

        elif choice == "settings" or choice == "sects" or choice == "sections" or choice == "st":
            print()
            for i in settings:
                print(" - "+i)

        elif choice == "dt" or choice == "date and time" or choice == "dateandtime" or choice == "d&t" or choice == "date & time":
            dt()

        elif choice == "mi" or choice == "my info" or choice == "myinfo" or choice == "info":
            mi()

        elif choice == "app settings" or choice == "appsettings" or choice == "as":
            appsettings()

        else:
            print("Invalid input. Please try again.\n")

    write = f"""
from datetime import datetime as dt

dtf = \"{dtf}\"
tf = \"{tf}\"
d = dt.now().strftime(dtf)
t = dt.now().strftime(tf)
username = \"{user}\"
password = \"{pw}\"
name = \"{name}\"
hcl = {hcl}
    """

    source = open("settingsource.py", "w")
    source.write(write)

# settings()
