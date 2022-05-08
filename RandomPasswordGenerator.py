def rpg():

    while True:

        import random as r

        global password

        chars = input("\nEnter the length of the password here (or type \'quit\' to quit): ")
        randInt = r.randint(0, 87)
        password = []
        pstr = ""


        def charAppend(pwd, num):

            if num == 10:
                pwd.append("A")
            elif num == 11:
                pwd.append("B")
            elif num == 12:
                pwd.append("C")
            elif num == 13:
                pwd.append("D")
            elif num == 14:
                pwd.append("E")
            elif num == 15:
                pwd.append("F")
            elif num == 16:
                pwd.append("G")
            elif num == 17:
                pwd.append("H")
            elif num == 18:
                pwd.append("I")
            elif num == 19:
                pwd.append("J")
            elif num == 20:
                pwd.append("K")
            elif num == 21:
                pwd.append("L")
            elif num == 22:
                pwd.append("M")
            elif num == 23:
                pwd.append("N")
            elif num == 24:
                pwd.append("O")
            elif num == 25:
                pwd.append("P")
            elif num == 26:
                pwd.append("Q")
            elif num == 27:
                pwd.append("R")
            elif num == 28:
                pwd.append("S")
            elif num == 29:
                pwd.append("T")
            elif num == 30:
                pwd.append("U")
            elif num == 31:
                pwd.append("V")
            elif num == 32:
                pwd.append("W")
            elif num == 33:
                pwd.append("X")
            elif num == 34:
                pwd.append("Y")
            elif num == 35:
                pwd.append("Z")
            elif num == 36:
                pwd.append("!")
            elif num == 37:
                pwd.append("@")
            elif num == 38:
                pwd.append("#")
            elif num == 39:
                pwd.append("$")
            elif num == 40:
                pwd.append("%")
            elif num == 41:
                pwd.append("^")
            elif num == 42:
                pwd.append("&")
            elif num == 43:
                pwd.append("*")
            elif num == 44:
                pwd.append("(")
            elif num == 45:
                pwd.append(")")
            elif num == 46:
                pwd.append("-")
            elif num == 47:
                pwd.append("_")
            elif num == 48:
                pwd.append("+")
            elif num == 49:
                pwd.append("=")
            elif num == 50:
                pwd.append(";")
            elif num == 51:
                pwd.append(":")
            elif num == 52:
                pwd.append("[")
            elif num == 53:
                pwd.append("]")
            elif num == 54:
                pwd.append("{")
            elif num == 55:
                pwd.append("}")
            elif num == 56:
                pwd.append("\\")
            elif num == 57:
                pwd.append("|")
            elif num == 58:
                pwd.append("<")
            elif num == 59:
                pwd.append(">")
            elif num == 60:
                pwd.append("/")
            elif num == 61:
                pwd.append("?")
            elif num == 62:
                pwd.append("a")
            elif num == 63:
                pwd.append("b")
            elif num == 64:
                pwd.append("c")
            elif num == 65:
                pwd.append("d")
            elif num == 66:
                pwd.append("e")
            elif num == 67:
                pwd.append("f")
            elif num == 68:
                pwd.append("g")
            elif num == 69:
                pwd.append("h")
            elif num == 70:
                pwd.append("i")
            elif num == 71:
                pwd.append("j")
            elif num == 72:
                pwd.append("k")
            elif num == 73:
                pwd.append("l")
            elif num == 74:
                pwd.append("m")
            elif num == 75:
                pwd.append("n")
            elif num == 76:
                pwd.append("o")
            elif num == 77:
                pwd.append("p")
            elif num == 78:
                pwd.append("q")
            elif num == 79:
                pwd.append("r")
            elif num == 80:
                pwd.append("s")
            elif num == 81:
                pwd.append("t")
            elif num == 82:
                pwd.append("u")
            elif num == 83:
                pwd.append("v")
            elif num == 84:
                pwd.append("w")
            elif num == 85:
                pwd.append("x")
            elif num == 86:
                pwd.append("y")
            elif num == 87:
                pwd.append("z")


        if chars == "q" or chars == "quit" or chars == "exit" or chars == "close":
            print("\nApp closed.")
            break

        else:

            chars = int(chars)

            for x in range(chars):

                if randInt < 10:

                    password.append(randInt)
                    randInt = r.randint(0, 87)

                else:

                    charAppend(password, randInt)
                    randInt = r.randint(0, 87)

            for y in range(chars):

                pstr = pstr+str(password[y])


            print("Here is your password:", pstr)

# rpg()