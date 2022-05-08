def taf():

    while True:

        import math

        method = input("Enter the method you want to use here(\'quit\' to quit, \'bxh\' for base and height or \'hf\' to use Heron's formula: ")

        if method == "q" or method == "quit" or method == "exit" or method == "close":
            print("\nApp Closed.")
            break

        elif method == "bxh":

            b = float(input("\nEnter the base here: "))
            h = float(input("Enter the height here: "))
            unit = input("Enter the unit in here: ")

            area = b * h / 2

            print("The area of this triangle is", str(area)+unit, "squared.")

        elif method == "hf":

            a = float(input("Enter the first side length in here: "))
            b = float(input("Enter the second side length in here: "))
            c = float(input("Enter the third side length in here: "))
            unit = input("Enter the unit in here: ")
            s = (a+b+c)/2
            asqr = s*(s-a)*(s-b)*(s-c)
            area = math.sqrt(asqr)

            print("The area of this triangle is", str(area)+unit, "squared.")

        else:
            print("Invalid input. Please try again.")