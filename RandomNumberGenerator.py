def rng():

    while True:

        import random

        digits = input("\nEnter the amount of digits you want to use - the number may take a bit to load if it has more than 100 000 digits (enter \'quit\' to quit): ")

        if digits == "quit" or digits == "q" or digits == "close" or digits == "exit":
            print("\nApp Closed.")
            break

        else:

            digits = int(digits)

            if digits == 1:
                print("Here is your number:", random.randint(0, 9))
            else:
                power1 = digits-1
                power2 = 10**digits
                numpar1 = 10**power1
                numpar2 = power2-1
                num = random.randint(numpar1, numpar2)
                print("Here is your number:", num)