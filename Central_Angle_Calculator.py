
def cac():

    print("\nCentral Angle Calculator (Circle Graphs):")

    while True:

        try:

            method = input("\nEnter the calculation method you would like to use in here (\'percentage\', \'quantity\' or \'quit\' to quit): ")

            if method == "quit" or method == "exit" or method == "q" or method == "close":
                print("\nApp Closed.")
                break

            elif method == "percentage" or method == "p" or method == "pct" or method == "P" or method == "Percentage" or method == "PCT" or method == "percent" or method == "Percent":

                p = float(input("Enter the percentage in here: "))
                angle = p*3.6

                print("The central angle for this section is", angle, end=" degrees.\n\n")

            elif method == "quantity" or method == "qu" or method == "QU" or method == "Quantity" or method == "qty" or method == "QTY":

                quantity = float(input("Enter the quantity of the section in here: "))
                total = float(input("Enter the total quantity of all sections in here: "))
                p = quantity/total*100
                angle = p*3.6

                if quantity > total:
                    quantity = input("Quantity is greater than total. Please enter a value less than or equal to the total: ")
                    total = float(input("Enter the total quantity of all sections in here: "))
                    p = quantity/total*100
                    angle = p*3.6

                else:
                    print("The central angle for this section is", angle, end=" degrees.\n")
                    print("This section accounts for", p, end="%")
                    print(" of the circle graph.")


            else:
                print("Invalid input. Please try again.")

        except:
            print("\nThere was an error. Please try again.\n")
