def calc():

    print("-" * (len("Calculator")) + "\nCalculator\n" + "-" * len("Calculator"))
    print("Note: All results will be rounded to the 7th decimal place.\n")

    import math

    def calculate(num1, op, num2):

        if num1.lower() == "pi":
            num1 = math.pi

        if num2.lower() == "pi":
            num2 = math.pi

        else:

            num1 = float(num1)
            num2 = float(num2)

            if op == "+" or op == "addition" or op == "add" or op == "plus" or op == "sum":
                print(round(num1 + num2, 7))

            elif op == "-" or op == "subtraction" or op == "subtract" or op == "minus":
                print(round(num1 - num2, 7))

            elif op == "x" or op == "*" or op == "multiplication" or op == "multiply" or op == "times":
                print(round(num1 * num2, 7))

            elif op == "/" or op == "division" or op == "divide" or op == "over" or op == "div":
                print(round(num1 / num2, 7))

            elif op == "remainderdivision" or op == "remainderdiv" or op == "divide with remainder" or op == "division with remainder" or op == "rd" or op == "find remainder" or op == "findremainder":
                print(f"{round(num1 // num2, 7)}\nRemainder: {num1 % num2}")

            elif op == "square root" or op == "sqrt" or op == "v" or op == "squareroot" or op == "root":
                print(round(math.sqrt(num1), 7))

            elif op == "to the power of" or op == "power" or op == "^":
                print(round(num1 ** num2, 7))

            elif op == "log" or op == "logarithm":
                print(round(math.log(num1, num2), 7))

            elif op == "factorial" or op == "!":
                print(round(math.factorial(num1), 7))


    while True:

        validops = ["+", "addition", "add", "plus", "sum", "-", "subtraction", "subtract", "minus", "x", "*", "multiplication", "multiply", "times", "/", "division", "divide", "over", "div", "remainderdivision", "remainderdiv", "divide with remainder", "division with remainder","rd", "find remainder", "findremainder", "square root", "sqrt", "v", "squareroot", "root", "to the power of", "power", "^", "log", "logarithm", "factorial", "!"]
        n1 = input("\nEnter the first number here (type \'pi\' if using pi or \'quit\' to quit the program): ")

        if n1 == "q" or n1 == "quit" or n1 == "exit" or n1 == "close":
            break

        else:

            try:
                op = input("Enter the operator here: ")

                if op in validops:
                    n2 = input("Enter the second number here (type \'pi\' if using pi): ")
                    calculate(n1, op, n2)

                else:
                    print("Invalid operator. please try again.")

            except:
                print("\nThere was an error. Please try again.\n")

    print("\nApp Closed.")
