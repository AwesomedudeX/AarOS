def gtn():

    import random

    print("\n\nGuess The Number")

    global rounds
    rounds = 0
    rounds -= 1
    wins = 0
    losses = 0
    errors = 0

    while True:

        rounds += 1


        print("\nRounds played:", rounds, "\n")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Errors:", errors)

        mode = input("\nEnter difficulty here (\'Easy\', \'Medium\', \'Hard\', \'Insane\', \'Impossible\', \'ImpossibleX\' or \'quit\' to quit): ")

        if mode == "quit" or mode == "q" or mode == "exit" or mode == "close":
            print("\nApp Closed.")
            break

        elif mode == "Easy" or mode == "easy" or mode == "ez" or mode == "e" or mode == "E" or mode == "EZ":
            num = int(random.randint(1, 10))
            print("I am thinking of a number between 1 and 10. What is it?")
            answer = int(input("Enter your guess here: "))

            if answer == num:
                print("\nYou win! Next round, coming up!")
                wins += 1

            elif answer > num:
                print("\nToo high! You lost. Try again in the next round!")
                losses += 1
            elif answer < num:
                print("\nToo low! You lost. Try again in the next round!")
                losses += 1

        elif mode == "Medium" or mode == "medium" or mode == "med" or mode == "Med" or mode == "mid" or mode == "Mid" or mode == "M" or mode == "m":
            num = int(random.randint(1, 100))
            print("I am thinking of a number between 1 and 100. What is it?")
            answer = int(input("Enter your guess here: "))

            if answer == num:
                print("\nYou win! Next round, coming up!")
                wins += 1

            elif answer > num:
                print("\nToo high! You lost. Try again in the next round!")
                losses += 1
            elif answer < num:
                print("\nToo low! You lost. Try again in the next round!")
                losses += 1


        elif mode == "Hard" or mode == "hard" or mode == "h" or mode == "H":
            num = int(random.randint(1, 1000))
            print("I am thinking of a number between 1 and 1000. What is it?")
            answer = int(input("Enter your guess here: "))

            if answer == num:
                print("\nYou win! Next round, coming up!")
                wins += 1

            elif answer > num:
                print("\nToo high! You lost. Try again in the next round!")
                losses += 1
            elif answer < num:
                print("\nToo low! You lost. Try again in the next round!")
                losses += 1


        elif mode == "Insane" or mode == "insane" or mode == "in" or mode == "In":
            num = int(random.randint(1, 10000))
            print("I am thinking of a number between 1 and 10 000. What is it?")
            answer = int(input("Enter your guess here: "))

            if answer == num:
                print("\nYou win! Next round, coming up!")
                wins += 1

            elif answer > num:
                print("\nToo high! You lost. Try again in the next round!")
                losses += 1
            elif answer < num:
                print("\nToo low! You lost. Try again in the next round!")
                losses += 1
            else:
                print("\nThat wasn't a valid answer. Please enter a valid answer in the next round.")
                errors += 1

        elif mode == "Impossible" or mode == "impossible" or mode == "im" or mode == "Im":
            num = int(random.randint(1, 100000))
            print("I am thinking of a number between 1 and 100 000. What is it?")
            answer = int(input("Enter your guess here: "))

            if answer == num:
                print("\nYou win! Next round, coming up!")
                wins += 1

            elif answer > num:
                print("\nToo high! You lost. Try again in the next round!")
                losses += 1
            elif answer < num:
                print("\nToo low! You lost. Try again in the next round!")
                losses += 1

        elif mode == "ImpossibleX" or mode == "impossibleX" or mode == "imx" or mode == "Imx" or mode == "Impossiblex" or mode == "impossiblex" or mode == "ImX" or mode == "imX":
            num = int(random.randint(1, 1000000))
            print("I am thinking of a number between 1 and 1 000 000. What is it?")
            answer = int(input("Enter your guess here: "))

            if answer == num:
                print("\nYou win! Next round, coming up!")
                wins += 1

            elif answer > num:
                print("\nToo high! You lost. Try again in the next round!")
                losses += 1
            elif answer < num:
                print("\nToo low! You lost. Try again in the next round!")
                losses += 1

        else:
            print("\nThere was an error.")
            errors += 1
