def calc():

    import math

    def calculate(num1, op, num2):

        if num1 == "-0":
            num1 = math.pi

        if num2 == -0:
            num2 = math.pi

        if op == "+" or op == "addition" or op == "add" or op == "plus" or op == "sum":
            print(num1 + num2)

        elif op == "-" or op == "subtraction" or op == "subtract" or op == "minus":
            print(num1 - num2)

        elif op == "x" or op == "*" or op == "multiplication" or op == "multiply" or op == "times":
            print(num1 * num2)

        elif op == "÷" or op == "/" or op == "division" or op == "divide" or op == "over" or op == "div":
            print(num1 / num2)

        elif op == "remainderdivision" or op == "remainderdiv" or op == "divide with remainder" or op == "division with remainder" or op == "rd" or op == "find remainder" or op == "findremainder":
            print(num1 // num2, "\nRemainder:", num1 % num2)

        elif op == "square root" or op == "sqrt" or op == "√" or op == "v" or op == "squareroot" or op == "root":
            print(math.sqrt(num1))

        elif op == "to the power of" or op == "power" or op == "^":
            print(num1 ** num2)

        elif op == "log" or op == "logarithm":
            print(math.log(num1, num2))

        elif op == "factorial" or op == "!":
            print(math.factorial(num1))


    while True:

        validops = ["+", "addition", "add", "plus", "sum", "-", "subtraction", "subtract", "minus", "x", "*", "multiplication", "multiply", "times", "÷", "/", "division", "divide", "over", "div", "remainderdivision", "remainderdiv", "divide with remainder", "division with remainder","rd", "find remainder", "findremainder", "square root", "sqrt", "√", "v", "squareroot", "root", "to the power of", "power", "^", "log", "logarithm", "factorial", "!"]
        n1 = input("\nEnter the first number here (type \'-0\' if using pi or \'quit\' to quit the program): ")

        if n1 == "q" or n1 == "quit" or n1 == "exit" or n1 == "close":
            break

        else:

            n1 = float(n1)
            op = input("Enter the operator here: ")

            if op in validops:
                n2 = float(input("Enter the second number here (type \'-0\' if using pi): "))

                calculate(n1, op, n2)

            else:
                print("Invalid operator. please try again.")

    print("\nApp Closed.")
