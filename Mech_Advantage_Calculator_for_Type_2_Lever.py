def MACT2L():


    while True:

        calctype = input("\n\nWhat do you want to calculate (total work - Joules, new effort force - Newtons, current effort force - Newtons, mechanical advantage - %, or type \'quit\' to quit)?\n\n")

        if calctype == "quit" or calctype == "q" or calctype == "close" or calctype == "exit":
            print("App Closed.")
            break

        elif calctype == "new effort force":

            prevwr = float(input("Enter the previous effort arm length in here (meters): "))
            prevef = float(input("Enter the previous effort force in here (Newtons): "))
            wr = float(input("Enter the effort arm length in here (meters): "))
            ef = prevwr*prevef/wr

            if prevwr > wr:
                print("New effort arm length is smaller than previous effort arm length; force needed will increase, leading to an efficiency decline.")

            else:
                print("New effort force is", ef, "Newtons.")
                print("Force reduction is", prevef/ef*100-100, end="%")

        elif calctype == "current effort force":

            w = float(input("Please enter the total work in here (Joules): "))
            wr = float(input("Please enter the effort arm length in here (meters): "))
            ef = w/wr

            print("Effort force is", ef, "Newtons.")

        elif calctype == "total work":

            wr = float(input("Please enter the effort arm length in here (meters): "))
            ef = float(input("Please enter the effort force in here (Newtons): "))
            w = ef*wr

            print("Total work is", w, "Joules.")

        elif calctype == "mechanical advantage" or calctype == "ma" or calctype == "MA" or calctype == "mech advantage":

            wt = float(input("Enter the weight of the load in here (Newtons): "))
            wr = float(input("Enter the effort arm length in here (meters): "))
            ef = wt/wr
            ma = str(wt/ef-1)

            print("Effort force needed:", wt/wr, "Newtons.")
            print("Mechanical advantage:", ma+"x", "force amplification.")

        else:
            print("Invalid input; please try again.\n\n")


# MACT2L()