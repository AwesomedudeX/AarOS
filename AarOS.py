def aarOS():

    import time
    import settingsource as ss
    from datetime import datetime as dt

    applist = [
        " - AarOS App Manager (am)",
        " - Binomial Distribution Calculator (bdc)",
        " - Calculator (calc)",
        " - Central Angle Calculator (cac)",
        " - Charts (ct)",
        " - Checklist (cl)",
        " - Charts Texture Dictionary (ctd)",
        " - DataFrames (df)",
        " - AarOS Fit (fit)",
        " - File Manager (fm)",
        " - Guess The Number (gtn)",
        " - Morse Code Converter (mcc)",
        " - Random Number Generator (rng)",
        " - Random Password Generator (rpg)",
        " - Rock Paper Scissors (rps)",
        " - Settings",
        " - Triangle Area Finder (taf)"
    ]

    def home():

        print("\n" + "-" * 13 + "\nAarOS Console\n" + "-" * 13)
        print("\nDate: ", dt.now().strftime(ss.dtf))
        print("Time: ", dt.now().strftime(ss.tf))

        if ss.hcl == True:
            import checklistsource as cls
            print("\nChecklist:\n")
            for i in range(len(cls.cl)):
                print(str(i + 1) + ". ", cls.cl[i])

        else:
            pass

    def login():

        while True:

            username = ss.username
            pwd = ss.password
            usr = input("\nUsername (enter \'shutdown\' to shut AarOS down): ")

            if username != "quit" and username != "q" and username != "close" and username != "exit":

                if usr == "shutdown" or usr == "quit" or usr == "q" or usr == "close" or usr == "exit" and username != "shutdown":
                    print("\nShutting Down...")
                    exit(0)

                else:

                    pw = input("Password: ")

                    if usr == username and pw == pwd:

                        if ss.name != "":
                            print("\n" * 100)
                            print(f"\nWelcome, {ss.name}!")
                            break
                        else:
                            break

                    else:
                        print("Username and/or password is wrong. Please try again.")

    def apps():

        while True:

            app = input("\n\nWhat app would you like to open (type \"home\" to go back to the home page)? ").lower()
            print("\n\n")

            if app == "home" or app == "back" or app == "return" or app == "q" or app == "quit" or app == "close" or app == "exit":
                break

            else:

                if app == "appmanager" or app == "app manager" or app == "am":
                    import AppManager
                    AppManager.appmanager()

                if app == "binomial distribution calculator" or app == "bdc" or app == "binomial_distribution_calculator":
                    import Binomial_Distribution_Calculator as bdc
                    bdc.bdc()

                if app == "calculator" or app == "calc":
                    import Calculator as calc
                    calc.calc()

                if app == "central angle calculator" or app == "cac" or app == "central_angle_calculator":
                    import Central_Angle_Calculator as cac
                    cac.cac()

                if app == "charts" or app == "ct":
                    import Charts as ct
                    ct.charts()

                if app == "checklist" or app == "cl":
                    import Checklist
                    Checklist.cl()

                if app == "ctd" or app == "chart texture dictionary" or app == "charttexturedictionary":
                    import ChartTextureDictionary as ctd
                    ctd.ctd()

                if app == "df" or app == "dataframes" or app == "dataframe" or app == "dfs":
                    import DataFrames as dfs
                    dfs.df()



                if app == "file_manager" or app == "fm" or app == "file manager":
                    import File_Manager as fm
                    fm.fm()

                if app == "gtn" or app == "guess the number" or app == "guess_the_number":
                    import Guess_The_Number as gtn
                    gtn.gtn()

                if app == "morse code converter" or app == "morsecodeconverter" or app == "morse_code_converter" or app == "mcc":
                    import Morse_Code_Converter as mcc
                    mcc.mcc()

                if app == "rng" or app == "randomnumbergenerator" or app == "random number generator":
                    import RandomNumberGenerator as rng
                    rng.rng()

                if app == "random password generator" or app == "rpg" or app == "randompasswordgenerator":
                    import RandomPasswordGenerator as rpg
                    rpg.rpg()

                if app == "rock paper scissors" or app == "rock_paper_scissors" or app == "rps":
                    import Rock_Paper_Scissors as rps
                    rps.rps()

                if app == "settings":
                    import Settings
                    Settings.settings()

                if app == "triangleareafinder" or app == "triangle area finder" or app == "taf":
                    import TriangleAreaFinder as taf
                    taf.taf()

        home()

    home()

    if ss.username != "" and ss.password != "":
        login()
    else:
        pass


    while True:

        start = input("\nWhat would you like to do (type \'list\' to list AarOS apps, \'shutdown\' to shut AarOS down or \'open\' to open an app)? ")

        if start == "q" or start == "quit" or start == "close" or start == "exit" or start == "shutdown":
            print("\nShutting Down...")
            time.sleep(1)
            exit(0)

        elif start == "list" or start == "l":
            print("\n(Note: This is a list of all apps available for download on AarOS; not a list of installed apps)\n")
            for i in applist:
                print(i)

        elif start == "open" or start == "o":
            apps()

        elif start not in applist:
            print("Invalid input. Please try again.")


aarOS()
