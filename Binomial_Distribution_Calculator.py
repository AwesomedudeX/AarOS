
def bdc():

    print("\n" + "-" * len("Binomial Distribution Calculator") + "\nBinomial Distribution Calculator\n" + "-" * len("Binomial Distribution Calculator"))
    print("(Disclaimer: All results for this calculator will be rounded to the 7th decimal place to prevent glitches)\n")

    def factorial(n):

        total = 1

        for i in range(n):
            total *= i + 1

        if n < 0:
            print("Negative values are invalid.")
            return None

        else:
            return total

    def pcbd():

        try:
            n = int(input("\nEnter the total number of events that you want to use: "))
            sub = int(input("Enter the total number of possibilities that there are for each event: "))
            sp = int(input("Enter the total number of possibilities for each event that are successful: "))
            r = int(input("Enter the total number of events that you want to be successful: "))

            s = sp / sub
            f = 1 - s

            ways = factorial(n) / (factorial(r) * factorial(n - r))
            prob = s ** r * f ** (n - r) * ways

            if r == 1:
                print(f"The probability of the event being successful in this case is {round(prob, 9) * 100}%.")
            else:
                print(f"The probability of {r} out of {n} events being successful in this case is {round(prob, 9) * 100}%.")

        except:
            print("\nThere was an error. Please try again.\n")

    desc = """
Binomial distributions are used to figure out probabilities of double-layered possibilities. What this means, is that instead of finding the probability of getting
say 1 of 5 possibilities, you'd be trying to find the probability of maybe 2 of 10 events being successful when each event has 5 possibilities with 3 of them
resulting in success. Now, I'll break this process down into steps that you can use to calculate binomial distributions.

First, we'll need the actual values for this. In this case, they'll be the values used in the example I gave before; 10 events each with 3 out of 5 possibilities
being successful, and we'll want 2 to be successful. Once you have these values, we'll need to get the success rate for each one by dividing the amount of
successful possibilities by the amount of possibilities for each event, or 3/5 to get 0.6. After this, we'll just subtract this rate from 1 to get the rate of failure,
which would be 0.4.

Next, we'll need to calculate the number of ways we can get 2 out of 10 events successful with these parameters. To do this, divide the factorial of the total number
of events by the product of the number of events that we want to be successful and the difference of the total number of events and the number of events that we want
to be successful, or 10!/2! x (10 - 2)!, which would be 45.

Finally, we'll need to calculate the actual probability of these conditions being true. To do this, raise the success rate to the power of the number of events that we
want to be successful, or 0.6^2, which gets us 0.36. Then, multiply that by the failure rate raised to the power of the difference of the total number of events and the
number of events that we want to be successful, or 0.36 x 0.4^(10-2), which gets us 0.0002359296 (it's a long decimal - I know, but this is how it'll be when you're
calculating binomials). Once you've done all that, multiply this by the number of ways that we can get the result that we want, or 0.0002359296 x 45, which gives us
a probability of 0.010616832, or 1.0616832% if we multiply it by 100.

I know this is a long process, but it can be pretty useful at times. The fact that it's a long process is also why I created this calculator, so I hope that this
explanation helps you understand what's really going on behind the scenes.

"""

    while True:

        choice = input("\nWhat do you want to do (\'calc\' to start the calculator, \'desc\' to view the description of what binomial distributions are or \'quit\' to quit)? ").lower()

        if choice == "q" or choice == "quit" or choice == "exit" or choice == "close":
            print("\nApp closed.")
            break

        elif choice == "calc" or choice == "start" or choice == "calculator" or choice == "c" or choice == "s":
            pcbd()

        elif choice == "desc" or choice == "description" or choice == "describe":
            print(desc)

        else:
            print("Invalid input. Please try again.\n")
