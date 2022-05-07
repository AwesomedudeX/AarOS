def mcc():
    def mte(s):

        l = []
        e = ""
        y = ""

        s.append(" ")
        s.append("/")

        for x in s:

            if x == "/":
                l.append(" ")

            elif x == " ":

                if y == ".-" or y == "*-":
                    l.append("A")

                elif y == "-..." or y == "-***":
                    l.append("B")

                elif y == "-.-." or y == "-*-*":
                    l.append("C")

                elif y == "-.." or y == "-**":
                    l.append("D")

                elif y == "." or y == "*":
                    l.append("E")

                elif y == "..-." or y == "**-*":
                    l.append("F")

                elif y == "--." or y == "--*":
                    l.append("G")

                elif y == "...." or y == "****":
                    l.append("H")

                elif y == ".." or y == "**":
                    l.append("I")

                elif y == ".---" or y == "*---":
                    l.append("J")

                elif y == "-.-" or y == "-*-":
                    l.append("K")

                elif y == ".-.." or y == "*-**":
                    l.append("L")

                elif y == "--":
                    l.append("M")

                elif y == "-." or y == "-*":
                    l.append("N")

                elif y == "---":
                    l.append("O")

                elif y == ".--." or y == "*--*":
                    l.append("P")

                elif y == "--.-" or y == "--*-":
                    l.append("Q")

                elif y == ".-." or y == "*-*":
                    l.append("R")

                elif y == "..." or y == "***":
                    l.append("S")

                elif y == "-":
                    l.append("T")

                elif y == "..-" or y == "**-":
                    l.append("U")

                elif y == "...-" or y == "***-":
                    l.append("V")

                elif y == ".--" or y == "*--":
                    l.append("W")

                elif y == "-..-" or y == "-**-":
                    l.append("X")

                elif y == "-.--" or y == "-*--":
                    l.append("Y")

                elif y == "--.." or y == "--**":
                    l.append("Z")

                elif y == "-----":
                    l.append("0")

                elif y == ".----" or y == "*----":
                    l.append("1")

                elif y == "..---" or y == "**---":
                    l.append("2")

                elif y == "...--" or y == "***--":
                    l.append("3")

                elif y == "....-" or y == "****-":
                    l.append("4")

                elif y == "....." or y == "*****":
                    l.append("5")

                elif y == "-...." or y == "-****":
                    l.append("6")

                elif y == "--..." or y == "--***":
                    l.append("7")

                elif y == "---.." or y == "---**":
                    l.append("8")

                elif y == "----." or y == "----*":
                    l.append("9")

                elif y == ".-.-.-"  or y == "*-*-*-":
                    l.append(".")

                elif y == "--..--" or y == "--**--":
                    l.append(",")

                elif y == "---..." or y == "---***":
                    l.append(":")

                elif y == "..--.." or y == "**--**":
                    l.append("?")

                elif y == ".----." or y == "*----*":
                    l.append("\'")

                elif y == "-....-" or y == "-****-":
                    l.append("-")

                elif y == ".-..-." or y == "*-**-*":
                    l.append("\"")

                elif y == "-.-.--" or y == "-*-*--":
                    l.append("!")

                y = ""

            else:
                y = y+x

        for i in l:
            e = e+str(i)

        print(e)

    def etm(s):

            l = []
            m = ""

            for x in s:

                if x == "A" or x == "a":
                    l.append(".-")

                elif x == "B" or x == "b":
                    l.append("-...")

                elif x == "C" or x == "c":
                    l.append("-.-.")

                elif x == "D" or x == "d":
                    l.append("-..")

                elif x == "E" or x == "e":
                    l.append(".")

                elif x == "F" or x == "f":
                    l.append("..-.")

                elif x == "G" or x == "g":
                    l.append("--.")

                elif x == "H" or x == "h":
                    l.append("....")

                elif x == "I" or x == "i":
                    l.append("..")

                elif x == "J" or x == "j":
                    l.append(".---")

                elif x == "K" or x == "k":
                    l.append("-.-")

                elif x == "L" or x == "l":
                    l.append(".-..")

                elif x == "M" or x == "m":
                    l.append("--")

                elif x == "N" or x == "n":
                    l.append("-.")

                elif x == "O" or x == "o":
                    l.append("---")

                elif x == "P" or x == "p":
                    l.append(".--.")

                elif x == "Q" or x == "q":
                    l.append("--.-")

                elif x == "R" or x == "r":
                    l.append(".-.")

                elif x == "S" or x == "s":
                    l.append("...")

                elif x == "T" or x == "t":
                    l.append("-")

                elif x == "U" or x == "u":
                    l.append("..-")

                elif x == "V" or x == "v":
                    l.append("...-")

                elif x == "W" or x == "w":
                    l.append(".--")

                elif x == "X" or x == "x":
                    l.append("-..-")

                elif x == "Y" or x == "y":
                    l.append("-.--")

                elif x == "Z" or x == "z":
                    l.append("--..")

                elif x == "0":
                    l.append("-----")

                elif x == "1":
                    l.append(".----")

                elif x == "2":
                    l.append("..---")

                elif x == "3":
                    l.append("...--")

                elif x == "4":
                    l.append("....-")

                elif x == "5":
                    l.append(".....")

                elif x == "6":
                    l.append("-....")

                elif x == "7":
                    l.append("--...")

                elif x == "8":
                    l.append("---..")

                elif x == "9":
                    l.append("----.")

                elif x == ".":
                    l.append(".-.-.-")

                elif x == ",":
                    l.append("--..--")

                elif x == ":":
                    l.append("---...")

                elif x == "?":
                    l.append("..--..")

                elif x == "\'":
                    l.append(".----.")

                elif x == "-":
                    l.append("-....-")

                elif x == "\"":
                    l.append(".-..-.")

                elif x == "!":
                    l.append("-.-.--")
                elif x == " ":
                    l.append("/")

                else:
                    print(x, "is an invalid character.")

            m = m + l[0]

            for y in l[1:]:
                m = m + " " + y

            print(m)


    while True:

        cm = input("\nEnter m-e for Morse to English, e-m for English to Morse or \'quit\' to quit: ")

        if cm == 'q' or cm == "quit" or cm == "close":
            print("\nApp Closed.")
            break

        elif cm == "e-m" or cm == "etm":
            ui = list(input("Enter the message you want to convert to morse here: "))
            etm(ui)

        elif cm == "m-e" or cm == "mte":
            ui = list(input("Enter the message you want to convert to english here (letters with a space between them and words with \" / \" between them): "))
            mte(ui)

        else:
            print("Invalid input. Please try again.")


# mcc()