hist = []
choices = ["Rock", "Paper", "Scissors"]
wins = 0
losses = 0
ivd = 0
rnds = 1

def rps():

    print("\n\n"+"-"*len("Rock, Paper Scissors")+"\nRock, Paper Scissors\n"+"-"*len("Rock, Paper Scissors"))

    global wins, losses, ivd, rnds, choices

    def check():

        global wins, losses, ivd, rnds, choices

        if com == user:

            print("Tie! Both of us chose", choices[com] + "!")

        else:


            if user == 0 and com == 1:
                print("You lost! You chose", choices[user], "and I chose", choices[com], end=".\n")
                losses += 1

            elif user == 0 and com == 2:
                print("You won! You chose", choices[user], "and I chose", choices[com], end=".\n")
                wins += 1

            elif user == 1 and com == 0:
                print("You won! You chose", choices[user], "and I chose", choices[com], end=".\n")
                wins += 1

            elif user == 1 and com == 2:
                print("You lost! You chose", choices[user], "and I chose", choices[com], end=".\n")
                losses += 1

            elif user == 2 and com == 0:
                print("You lost! You chose", choices[user], "and I chose", choices[com], end=".\n")
                losses += 1

            elif user == 2 and com == 1:
                print("You won! You chose", choices[user], "and I chose", choices[com], end=".\n")
                wins += 1

    while True:

        print("\nRound:", rnds)
        print("Score:", str(wins) + "-" + str(losses), "(you-me)")
        print("Invalid Rounds:", ivd)

        import random as rnd


        ui = input("\n\nRock, Paper, or Scissors (type \'quit\' to quit or \'history\' to check the current game's history)? ")
        com = rnd.randint(0, 2)


        if ui == "q" or ui == "quit" or ui == "exit" or ui == "close":

            print("Good Game!", "The score is", str(wins)+"-"+str(losses), "(you-me).")
            print("\nApp Closed.")
            break

        elif ui == "history" or ui == "h" or ui == "hist" or ui == "recent":

            print("\nGame History (you-me):\n")

            if hist == []:
                print("Play a round to add it to the history!\n\n")

            else:
                for h in hist:
                    print(h)

        else:

            if ui == "Rock" or ui == "r" or ui == "rock" or ui == "R" or ui == 1:
                user = 0
                check()

            elif ui == "Paper" or ui == "p" or ui == "paper" or ui == "P" or ui == 2:
                user = 1
                check()

            elif ui == "Scissors" or ui == "s" or ui == "scissors" or ui == "S" or ui == 3:
                user = 2
                check()

            else:
                print("\nInvalid Choice. Please try again.")
                ivd += 1

            rnds += 1
            rhist = "Round "+str(rnds)+": "+ui+" VS "+choices[com]+": "+str(wins)+"-"+str(losses)
            hist.append(rhist)

# rps()


