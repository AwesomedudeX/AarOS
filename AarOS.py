def aarOS():

    from datetime import datetime as dt

    def home():

        dtf = "%B %d, %Y"
        tf = "%I:%M:%S %p"
        osdate = dt.now().strftime(dtf)
        ostime = dt.now().strftime(tf)
        print("\n" + "-" * 13 + "\nAarOS Console\n" + "-" * 13)
        print("\nDate: ", osdate)
        print("Time: ", ostime)

    def login():

        while True:

            username = "Awesomedude"
            pwd = "1162008"
            usr = input("\nUsername (enter \'shutdown\' to shut AarOS down): ")

            if usr == "shutdown" or usr == "quit" or usr == "q" or usr == "close" or usr == "exit":
                print("\nShutting Down...")
                exit(0)

            else:

                pw = input("Password: ")

                if usr == username and pw == pwd:
                    print("\nWelcome, Aarish Ayyasami!")
                    break

                else:
                    print("Username and/or password is wrong. Please try again.")

    def apps():

        while True:

            app = input("\n\nWhat app would you like to open (type \"home\" to go back to the home page)? ")

            if app == "home" or app == "back" or app == "return" or app == "q" or app == "quit" or app == "close" or app == "exit":
                home()
                break

            if app == "Calculator" or app == "calc":
                import calculator as calc
                calc.calc()

            if app == "Central Angle Calculator" or app == "cac" or app == "Central_Angle_Calculator":
                import Central_Angle_Calculator as cac
                cac.cac()

            if app == "charts" or app == "Charts" or app == "ct":
                import Charts as ct
                ct.charts()

            if app == "Checklist" or app == "checklist" or app == "cl":
                import Checklist
                Checklist.cl()

            if app == "ctd" or app == "Chart Texture Dictionary" or app == "ChartTextureDictionary":
                import ChartTextureDictionary as ctd
                ctd.ctd()

            if app == "File_Creator_and_Editor" or app == "fce" or app == "File Creator and Editor":
                import File_Creator_and_Editor as fce
                fce.fce()

            if app == "gtn" or app == "Guess The Number" or app == "Guess_The_Number":
                import Guess_The_Number as gtn
                gtn.gtn()

            if app == "mac" or app == "MACT2L" or app == "Mechanical Advantage Calculator - Type 2 Lever":
                import Mech_Advantage_Calculator_for_Type_2_Lever as mac
                mac.MACT2L()

            if app == "Morse Code Converter" or app == "MorseCodeConverter" or app == "Morse_Code_Converter" or app == "mcc":
                import Morse_Code_Converter as mcc
                mcc.mcc()

            if app == "Python Library Dictionary" or app == "pld" or app == "Python_Library_Dictionary":
                import Python_Library_Dictionary as pld
                pld.pld()

            if app == "pn" or app == "Python Notes" or app == "Python_Notes":
                import Python_Notes as pn
                pn.pn()

            if app == "rng" or app == "RandomNumberGenerator" or app == "Random Number Generator":
                import RandomNumberGenerator as rng
                rng.rng()

            if app == "Random Password Generator" or app == "rpg" or app == "RandomPasswordGenerator":
                import RandomPasswordGenerator as rpg
                rpg.rpg()

            if app == "Rock Paper Scissors" or app == "Rock_Paper_Scissors" or app == "rps":
                import Rock_Paper_Scissors as rps
                rps.rps()

            if app == "TriangleAreaFinder" or app == "Triangle Area Finder" or app == "taf":
                import TriangleAreaFinder as taf
                taf.taf()


    home()
    login()


    while True:

        start = input("\nWhat would you like to do (type \'list\' to list available apps, \'shutdown\' to shut AarOS down or \'open\' to open an app)? ")

        applist = [
            " - Calculator (calc)",
            " - Charts (ct)",
            " - Checklist (cl)",
            " - Clock",
            " - Charts Texture Dictionary (ctd)",
            " - File Creator and Editor (fce)",
            " - Guess The Number (gtn)",
            " - Mechanical Advantage Calculator - Type 2 Lever (mac)",
            " - Morse Code Converter (mcc)",
            " - Python Library Dictionary (pld)",
            " - Python Notes (pn)",
            " - Random Number Generator (rng)",
            " - Random Password Generator (rpg)",
            " - Rock Paper Scissors (rps)",
            " - Triangle Area Finder (taf)"
        ]


        if start == "q" or start == "quit" or start == "close" or start == "exit" or start == "shutdown":
            print("\nShutting Down...")
            exit(0)

        elif start == "list" or start == "l":
            print("")
            for i in applist:
                print(i)

        elif start == "open" or start == "o":
            apps()

        elif start not in applist:
            print("Invalid input. Please try again.")



aarOS()