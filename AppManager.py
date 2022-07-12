def appmanager():

    import os

    print("-"*len("AarOS App Manager")+"\nAarOS App Manager\n"+"-"*len("AarOS App Manager"))
    print("Note: Console must be restarted for App Store changes to be saved - the console will shutdown after this app is closed.")

    print("\nLoading...\n")

    bdc = """
def bdc():

    print(\"\\n\" + \"-\" * len(\"Binomial Distribution Calculator\") + \"\\nBinomial Distribution Calculator\\n\" + \"-\" * len(\"Binomial Distribution Calculator\"))
    print(\"(Disclaimer: All results for this calculator will be rounded to the 7th decimal place to prevent glitches)\\n\")

    def factorial(n):

        total = 1

        for i in range(n):
            total *= i + 1

        if n < 0:
            print(\"Negative values are invalid.\")
            return None

        else:
            return total

    def pcbd():

        try:

            n = int(input(\"\\nEnter the total number of events that you want to use: \"))
            sub = int(input(\"Enter the total number of possibilities that there are for each event: \"))
            sp = int(input(\"Enter the total number of possibilities for each event that are successful: \"))
            r = int(input(\"Enter the total number of events that you want to be successful: \"))
    
            s = sp / sub
            f = 1 - s
    
            ways = factorial(n) / (factorial(r) * factorial(n - r))
            prob = s ** r * f ** (n - r) * ways
    
            if r == 1:
                print(f\"The probability of the event being successful in this case is {round(prob, 9) * 100}%.\")
            else:
                print(f\"The probability of {r} out of {n} events being successful in this case is {round(prob, 9) * 100}%.\")

        except:
            print("There was an error. Please try again.")

    desc = \"\"\"
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

\"\"\"

    while True:

        choice = input(\"\\nWhat do you want to do (\\\'calc\\\' to start the calculator, \\\'desc\\\' to view the description of what binomial distributions are or \\\'quit\\\' to quit)? \").lower()

        if choice == \"q\" or choice == \"quit\" or choice == \"exit\" or choice == \"close\":
            print("\\nApp closed.\")
            break

        elif choice == \"calc\" or choice == \"start\" or choice == \"calculator\" or choice == \"c\" or choice == \"s\":
            pcbd()

        elif choice == \"desc\" or choice == \"description\" or choice == \"describe\":
            print(desc)

        else:
            print(\"Invalid input. Please try again.\\n\")
"""
    calc = """
def calc():

    print(\"-\" * (len(\"Calculator\")) + \"\\nCalculator\\n\" + \"-\" * len(\"Calculator\"))
    print(\"Note: All results will be rounded to the 7th decimal place.\\n\")

    import math

    def calculate(num1, op, num2):

        if num1 == \"-0\":
            num1 = math.pi

        if num2 == \"-0\":
            num2 = math.pi

        if op == \"+\" or op == \"addition\" or op == \"add\" or op == \"plus\" or op == \"sum\":
            print(round(num1 + num2, 7))

        elif op == \"-\" or op == \"subtraction\" or op == \"subtract\" or op == \"minus\":
            print(round(num1 - num2, 7))

        elif op == \"x\" or op == \"*\" or op == \"multiplication\" or op == \"multiply\" or op == \"times\":
            print(round(num1 * num2, 7))

        elif op == \"/\" or op == \"division\" or op == \"divide\" or op == \"over\" or op == \"div\":
            print(round(num1 / num2, 7))

        elif op == \"remainderdivision\" or op == \"remainderdiv\" or op == \"divide with remainder\" or op == \"division with remainder\" or op == \"rd\" or op == \"find remainder\" or op == \"findremainder\":
            print(round(num1 // num2, 7), \"\\nRemainder:", num1 % num2)

        elif op == \"square root\" or op == \"sqrt\" or op == \"v\" or op == \"squareroot\" or op == \"root\":
            print(round(math.sqrt(num1), 7))

        elif op == \"to the power of\" or op == \"power\" or op == \"^\":
            print(round(num1 ** num2, 7))

        elif op == \"log\" or op == \"logarithm\":
            print(round(math.log(num1, num2)), 7)

        elif op == \"factorial\" or op == \"!\":
            print(round(math.factorial(num1), 7))


    while True:

        validops = [\"+\", \"addition\", \"add\", \"plus\", \"sum\", \"-\", \"subtraction\", \"subtract\", \"minus\", \"x\", \"*\", \"multiplication\", \"multiply\", \"times\", \"/\", \"division\", \"divide\", \"over\", \"div\", \"remainderdivision\", \"remainderdiv\", \"divide with remainder\", \"division with remainder\",\"rd\", \"find remainder\", \"findremainder\", \"square root\", \"sqrt\", \"v\", \"squareroot\", \"root\", \"to the power of\", \"power\", \"^\", \"log\", \"logarithm\", \"factorial\", \"!\"]
        n1 = input(\"\\nEnter the first number here (type \\\'-0\\\' if using pi or \\\'quit\\\' to quit the program): \")

        if n1 == \"q\" or n1 == \"quit\" or n1 == \"exit\" or n1 == \"close\":
            break

        else:

            n1 = float(n1)
            op = input(\"Enter the operator here: \")

            if op in validops:
                n2 = float(input(\"Enter the second number here (type \\'-0\\' if using pi): \"))

                calculate(n1, op, n2)

            else:
                print(\"Invalid operator. please try again.\")

    print(\"\\nApp Closed.\")
"""
    cac = """
def cac():

    print(\"\\nCentral Angle Calculator (Circle Graphs):\")

    while True:

        method = input(\"\\nEnter the calculation method you would like to use in here (\\\'percentage\\\', \\\'quantity\\\' or \\\'quit\\\' to quit): \")

        if method == \"quit\" or method == \"exit\" or method == \"q\" or method == \"close\":
            print(\"\\nApp Closed.\")
            break

        elif method == \"percentage\" or method == \"p\" or method == \"pct\" or method == \"P\" or method == \"Percentage\" or method == \"PCT\" or method == \"percent\" or method == \"Percent\":

            p = float(input(\"Enter the percentage in here: \"))
            angle = p*3.6

            print(\"The central angle for this section is\", angle, end=\" degrees.\\n\\n\")

        elif method == \"quantity\" or method == \"qu\" or method == \"QU\" or method == \"Quantity\" or method == \"qty\" or method == \"QTY\":

            quantity = float(input(\"Enter the quantity of the section in here: \"))
            total = float(input(\"Enter the total quantity of all sections in here: \"))
            p = quantity/total*100
            angle = p*3.6

            if quantity > total:
                quantity = input(\"Quantity is greater than total. Please enter a value less than or equal to the total: \")
                total = float(input(\"Enter the total quantity of all sections in here: \"))
                p = quantity/total*100
                angle = p*3.6

            else:
                print(\"The central angle for this section is\", angle, end=\" degrees.\\n\")
                print(\"This section accounts for\", p, end=\"%\")
                print(\" of the circle graph.\")


        else:
            print(\"Invalid input. Please try again.\")
"""
    ct = """
def charts():

    print(\"\\n\" + \"-\" * 6 + \"\\nCharts\\n\" + \"-\" * 6 + \"\\n\")
    print(\"(Disclaimer: You may have to wait a few seconds to a minute for the program to create your chart; once you create one, you will need to close it to resume the app)\\n\\nLoading...\")

    import numpy as np
    import pandas as pd
    import seaborn as sn
    import matplotlib.pyplot as plt

    style = [
        [\"default\", \"The default look for all your charts.\"],
        [\"classic\", \" A vibrant, outlined chart texture.\"],
        [\"Solarize_Light2\", \"A chart texture that gives elements a brighter, more yellowish look.\"],
        [\"bmh\", \"A chart texture that gives elements a more greyish look, and adds a light grey grid in the background.\"],
        [\"dark_background\", \"A simple dark background for all your charts.\"],
        [\"fast\", \"Adds a bit more tone to the default texture.\"],
        [\"fivethirtyeight\", \"Adds more tone to the default texture and thickens lines in line graphs.\"],
        [\"ggplot\", \"Adds a reddish tint to the default texture.\"],
        [\"seaborn\", \"Adds a greyish tint to the default chart texture.\"],
        [\"seaborn-bright\", \"A brighter version of the seaborn chart texture.\"],
        [\"seaborn-colourblind\", \"A version of the seaborn chart texture optimized for the colourblind.\"],
        [\"seaborn-dark\", \"A combination of the seaborn chart texture and the default chart texture.\"],
        [\"seaborn-dark-palette\", \"The seaborn-bright texture, but with darker colours.\"],
        [\"seaborn-deep\", \"Adds a bit more tone to the original seaborn texture.\"],
        [\"seaborn-muted\", \"A brightened version of the original seaborn texture.\"],
        [\"seaborn-pastel\", \"An extremely brightened version of the original seaborn texture.\"],
        [\"tableau-colorblind10\", \"A version of the default texture optimized for the colourblind.\"]
    ]
    stylenames = [i[0] for i in style]


    def bp():

        url = input(\"Enter the full file download URL in here: \")
        section = input(\"What section do you want to use? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))

        sn.boxplot(data=file, x=file[section][s:e + 1])

    def hg():

        url = input(\"Enter the full file download URL in here: \")
        format = input(\"What format do you want to use (\\\'pyplot\\\' or \\\'seaborn\\\')? \")
        divs = int(input(\"How many divisions do you want in your histogram? \"))
        section = input(\"What section do you want to use? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))

        if format == \"pyplot\" or format == \"plt\" or format == \"matplotlib.pyplot\":
            plt.hist(url[section][s:e + 1], bins=divs)

        elif format == \"sn\" or format == \"sns\" or format == \"seaborn\":
            sn.displot(file[section][s:e + 1], bins=divs, kde=True)

        else:
            print(\"Invalid input. Please try again.\")

    def bar():

        url = input(\"Enter the full file download URL in here: \")
        section = input(\"What section do you want to use? \")
        palette = input(\"What colour palette would you like to use? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))
        addhue = input(\"Do you want to use category separation in your graph (y/n)? \")

        while True:

            if addhue.lower() == \"y\" or addhue.lower() == \"yes\":
                hue = input(\"What category do you want to use to separate the information? \")
                sn.countplot(x=section[s:e + 1], data=file, palette=palette, hue=hue)

            else:
                sn.countplot(x=section[s:e + 1], data=file, palette=palette)

    def line():

        url = input(\"Enter the full file download URL in here: \")
        section = input(\"What section do you want to use? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))
        y = np.arange(len(file[section][s:e]))
        format = input(\"What format do you want to use (pyplot - \\\'plt\\\' or seaborn \\\'sn\\\')? \")

        while True:

            if format == \"pyplot\" or format == \"plt\":

                cxt = input(
                    \"What colour and texture do you want to use - enter the starting letter of the colour followed by a texture (check Chart Texture Dictionary for textures)?\")
                print(\"(The section\", section, \"is on the x axis)\")
                plt.plot(file[section][s:e], y, cxt)
                break

            elif format == \"seaborn\" or format == \"sns\" or format == \"sn\":

                palette = input(\"What colour palette would you like to use? \")
                addhue = input(\"Do you want to use category separation in your graph (y/n)? \")

                while True:

                    if addhue.lower() == \"y\" or addhue.lower() == \"yes\":
                        hue = input(\"What category do you want to use to separate the information? \")
                        print(\"\\n(The section\", \"\\\'\" + section + \"\\\'\", \"is on the x axis)\")
                        sn.lineplot(data=file[s:e], x=section, y=y, palette=palette, hue=hue)
                        break

                    else:
                        print(\"\\n(The section\", \"\\\'\" + section + \"\\\'\", \"is on the x axis)\")
                        sn.lineplot(data=file[s:e], x=section, y=y, palette=palette)
                        break

                break

    def scatter():

        url = input(\"Enter the full file download URL in here: \")
        section = input(\"What section do you want to use? \")
        palette = input(\"What colour palette would you like to use? \")
        mkr = input(\"What marker would you like to use? \")
        size = int(input(\"What marker size (pixels) do you want to use? \"))

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))
        y = np.arange(len(file[section][s:e]))
        addhue = input(\"Do you want to use category separation in your graph (y/n)? \")

        while True:

            if addhue.lower() == \"y\" or addhue.lower() == \"yes\":
                hue = input(\"What category do you want to use to separate the information? \")
                print(\"\\n(The section\", \"\\\'\" + section + \"\\\'\", \"is on the x axis)\")
                sn.scatterplot(data=file[s:e], x=section, y=y, palette=palette, marker=mkr, size=size, hue=hue)
                break

            else:
                print(\"\\n(The section\", \"\\\'\" + section + \"\\\'\", \"is on the x axis)\")
                sn.scatterplot(data=file[s:e], x=section, y=y, palette=palette, marker=mkr, size=size)
                break

    def regplot():

        url = input(\"Enter the full file download URL in here: \")
        section = input(\"What section do you want to use? \")
        color = input(\"What colour would you like to use? \")
        mkr = input(\"What marker would you like to use? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))
        y = np.arange(len(file[section][s:e]))

        print(\"\\n(The section\", \"\\\'\" + section + \"\\\'\", \"is on the x axis)\")
        sn.regplot(x=file[section][s:e], y=y, color=color, marker=mkr)

    def pplt():

        url = input(\"Enter the full file download URL in here: \")
        palette = input(\"What colour palette would you like to use? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))

        sn.pairplot(file[s:e], palette=palette)

    def pie():

        url = input(\"Enter the full file download URL in here: \")
        section = input(\"What section do you want to use? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)

        while True:

            if section in file.columns:
                break
            else:
                print(\"Invalid section choice.\")
                return 0

        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \")) + 1
        sectnum = file[section].value_counts().shape[0]

        expl = []
        colours = []

        addexpl = input(\"Do you want to separate your pie chart sections from the center (y/n)? \")

        if addexpl.lower() == \"yes\" or addexpl.lower() == \"y\":

            for i in range(int(sectnum)):
                expl.append(
                    float(input(str(file[section].value_counts().index[i]) + \" category separation perentage: \")) / 100)

        else:
            expl = None

        addcolour = input(\"Do you want to customize your pie chart section colours (y/n)? \")

        if addcolour.lower() == \"yes\" or addcolour.lower() == \"y\":

            for x in range(int(sectnum)):
                y = x + 1
                i = input(\"Colour \" + str(y) + \" (\" + str(file[section].value_counts().index[x]) + \")\" + \": \").lower()
                colours.append(i)

        else:
            colours = None

        tc = input(\"What text colour do you want to use? \").lower()

        plt.pie(file[section][s:e].value_counts(), autopct=\"%1.2f%%\", labels=file[section][s:e].value_counts().index, shadow=True, colors=colours, explode=expl, textprops={\"color\": tc})

    def hm():

        url = input(\"Enter the full file download URL in here: \")
        colour = input(\"What colour would you like to use (enter in a valid heatmap colour format)? \")

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))

        print(\"Columns are represented in order - top to bottom and left to right.\")
        sn.heatmap(file[s:e].corr(), cmap=colour, annot=True)

    def jp():

        url = input(\"Enter the full file download URL in here: \")
        section = input(\"What section do you want to use? \")
        palette = input(\"What colour palette would you like to use? \")
        size = int(input(\"What graph side length (pixels) do you want to use? \"))

        print(\"\\nImporting file...\\n\")

        file = pd.read_csv(url)
        s = int(input(\"Enter the starting selection row number here: \"))
        e = int(input(\"Enter the ending selection row number here: \"))
        y = np.arange(len(file[section][s:e]))

        if section in file.columns:
            print()
        else:
            print(\"Invalid section.\")

        print(\"\\n(The section\", \"\\\'\" + section + \"\\\'\", \"is on the x axis)\")
        sn.jointplot(data=file[s:e], x=section, y=y, palette=palette, height=size)

    cts = [
        \"boxplot: \\\'bp\\\'\",
        \"histogram: \\\'hg\\\'\",
        \"bar graph: \\\'bar\\\'\",
        \"line graph: \\\'line\\\'\",
        \"scatter graph: \\\'scatter\\\'\",
        \"full-scale scatter graph (for the entire DataFrame): \'fss\'\",
        \"regression plot: \\\'regplot\\\'\",
        \"joint bar and scatter plot: \\\'jp\\\'\",
        \"pie chart: \\\'pie\\\'\",
        \"heatmap: \\\'hm\\\'\"
    ]

    while True:

        ctype = input(\"\\nWhat type of chart would you like to use (type \\\'ctypes\\\' to view chart types or \\\'quit\\\' to quit)? \").lower()

        if ctype == \"quit\" or ctype == \"q\" or ctype == \"exit\" or ctype == \"close\":
            print(\"\\nApp Closed.\")
            break

        elif ctype == \"ctypes\" or ctype == \"cts\" or ctype == \"chart types\":

            print()

            for i in cts:
                print(\" -\", i)

            print()

        else:

            title = input(\"What title would you like to use for your chart? \")
            bg = input(\"What chart style do you want to use (view Chart Texture Dictionary for chart styles)? \")

            if bg not in stylenames:
                print(\"Invalid chart style. Please try again.\")

            else:

                plt.style.use(bg)

                if ctype == \"bp\" or ctype == \"boxplot\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    bp()
                    plt.show()

                elif ctype == \"hg\" or ctype == \"histogram\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    hg()
                    plt.show()

                elif ctype == \"bar\" or ctype == \"bar graph\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    bar()
                    plt.show()

                elif ctype == \"line\" or ctype == \"line graph\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    line()
                    plt.show()

                elif ctype == \"scatter\" or ctype == \"scatter plot\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    scatter()
                    plt.show()

                elif ctype == \"regplot\" or ctype == \"regression plot\" or ctype == \"rplt\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    regplot()
                    plt.show()

                elif ctype == \"jp\" or ctype == \"jointplot\" or ctype == \"joint plot\" or ctype == \"jplt\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    jp()
                    plt.show()

                elif ctype == \"fss\" or ctype == \"pplt\" or ctype == \"full-scale scatter graph\" or ctype == \"pairplot\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    pplt()
                    plt.show()

                elif ctype == \"pie\" or ctype == \"pie chart\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    pie()
                    plt.show()

                elif ctype == \"hm\" or ctype == \"htmp\" or ctype == \"heatmap\" or ctype == \"heat map\":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    hm()
                    plt.show()

                elif ctype == \"jp\" or ctype == \"joint plot\" or ctype == \"jointplot\":
                    plt.title(title)
                    jp()
                    plt.show()

                else:
                    print(\"Invalid chart type. Please try again.\")


# charts()
# Test File: \"https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/meteorite-landings/meteorite-landings.csv\"

"""
    cl = """
def cl():

    print(\"\\n\\n\"+\"-\"*9+\"\\nChecklist\\n\"+\"-\"*9+\"\\n\")
    print(\"Note: Console must be shut down for Checklist changes to be saved.\")
    print(\"\\nLoading...\\n")

    import checklistsource as cls
    import os

    checklist = cls.cl

    def edit():

        item = int(input(\"Enter the number of the item you want to edit (or type \\\'return\\\' to go back): \"))

        if item != \"return\" and item != \"back\":
            modify = input(\"What do you want to change the item to? \")
            checklist[item-1] = modify
            print(\"Item modified successfully.\")

    actions = [
        \"Quit the app: \\\'quit\\\'\",
        \"View possible actions: \\\'actions\\\'\",
        \"List items in checklist: \\\'list\\\'\",
        \"Add an item to the checklist: \\\'add\\\'\",
        \"Change an item in the checklist: \\\'edit\\\'\",
        \"Delete an item in the checklist: \\\'delete\\\'\",
        \"Clear the checklist: \\\'clear\\\'\"
    ]

    while True:

        action = input(\"\\nWhat do you want to do (type \\\'actions\\\' for a list of things you can do)? \")

        if action == \"q\" or action == \"quit\" or action == \"close\" or action == \"exit\":
            print(\"\\nApp Closed.\")
            break

        elif action == \"actions\" or action == \"options\" or action == \"acts\" or action == \"opts\":
            print()
            for i in actions:
                print(\" - \", i)

        elif action == \"list\" or action == \"view\":
            print()
            for i in range(len(checklist)):
                print(str(i+1)+\". \", checklist[i])

        elif action == \"add\" or action == \"new\" or action == \"create\":
            add = input(\"What are you adding to your checklist? \")
            checklist.append(add)
            print(\"Item added successfully.\")

        elif action == \"change\" or action == \"edit\" or action == \"modify\":
            edit()

        elif action == \"del\" or action == \"delete\" or action == \"remove\":
            delete = int(input(\"\\nEnter the number for the item that you want to delete: \"))
            if delete <= len(checklist):
                checklist.pop(delete-1)
                print(\"Item\",  delete, \"deleted successfully.\")
            else:
                print(\"There is no item\", \"\\\'"+delete+\"\\\'\", \"in your checklist.\")


        elif action == \"reset\" or action == \"clear\":

            reset = input(\"Are you sure (y/n)? \")

            if reset == \"y\" or reset == \"Y\" or reset == \"Yes\" or reset == \"yes\":
                checklist = []
                print(\"Checklist was cleared successfully.\")
            elif reset == \"No\" or reset == \"no\" or reset == \"n\" or reset == \"N\":
                print()
            else:
                print(\"Invalid input.\")

        else:
            print(\"Invalid input. Please try again.\\n\")


    source = open(\"checklistsource.py\", \"w\")
    source.write(\"cl = [\")

    source = open(\"checklistsource.py\", \"a\")

    for i in range(len(checklist)-1):
        source.write(\"\\\"\"+checklist[i]+\"\\\"\"+\", \")

    if len(checklist) > 0:
        source.write(\"\\\"\" + checklist[len(checklist) - 1] + \"\\\"\" + \"]\")
    else:
        source.write(\"]\")
"""
    ctd = """
def ctd():

    print(\"\\n\" + \"-\" * len(\"Chart Texture Dictionary\") + \"\\nChart Texture Dictionary\\n\" + \"-\" * len(\"Chart Texture Dictionary\"))

    line = [
        \": | A simple dot texture.\",
        \"-- | A simple dotted line texture.\",
        \"- | A simple regular line texture\",
        \"-. | A dash-dot line pattern.\",
        \"-o | An enlarged point texture.\"
    ]

    style = [
        [\"default\", \"The default look for all your charts.\"],
        [\"classic\", \" A vibrant, outlined chart texture.\"],
        [\"Solarize_Light2\", \"A chart texture that gives elements a brighter, more yellowish look.\"],
        [\"bmh\", \"A chart texture that gives elements a more greyish look, and adds a light grey grid in the background.\"],
        [\"dark_background\", \"A simple dark background for all your charts.\"],
        [\"fast\", \"Adds a bit more tone to the default texture.\"],
        [\"fivethirtyeight\", \"Adds more tone to the default texture and thickens lines in line graphs.\"],
        [\"ggplot\", \"Adds a reddish tint to the default texture.\"],
        [\"seaborn\", \"Adds a greyish tint to the default chart texture.\"],
        [\"seaborn-bright\", \"A brighter version of the seaborn chart texture.\"],
        [\"seaborn-colourblind", \"A version of the seaborn chart texture optimized for the colourblind.\"],
        [\"seaborn-dark\", \"A combination of the seaborn chart texture and the default chart texture.\"],
        [\"seaborn-dark-palette\", \"The seaborn-bright texture, but with darker colours.\"],
        [\"seaborn-deep\", \"Adds a bit more tone to the original seaborn texture.\"],
        [\"seaborn-muted\", \"A brightened version of the original seaborn texture.\"],
        [\"seaborn-pastel\", \"An extremely brightened version of the original seaborn texture.\"],
        [\"tableau-colorblind10\", \"A version of the default texture optimized for the colourblind.\"]
    ]

    while True:

        ctype = input(\"\\nWhich texture type do you want to see (line graph textures - \\\'line\\\', style sheets - \\\'style\\\' or do you want to quit - \\\'quit\\\')? \").lower()

        if ctype == \"quit\" or ctype == \"q\" or ctype == \"exit\" or ctype == \"close\":
            print(\"\\nApp Closed.\")
            break

        elif ctype == \"line\" or ctype == \"plot\":
             for i in line:
                 print(\" -\", i)

        elif ctype == \"style\" or ctype == \"sheets\" or ctype == \"ss\":
            for i in style:
                print(\" -\", i[0]+\":\", i[1])

        else:
            print(\"Invalid input. Please try again.\\n\")
"""
    dfs = """
def df():

    print(\"-\"*len(\"DataFrames\")+\"\\nDataFrames\\n\"+\"-\"*len(\"DataFrames\"))
    print(\"Note: If more than 5 columns are selected, DataFrame will be displayed in mass rows with 5 columns displayed per row.\\n\\nLoading...\\n\\n\")

    import warnings
    import pandas as pd
    from sklearn.linear_model import LinearRegression as lreg
    from sklearn.model_selection import train_test_split as tts

    warnings.filterwarnings(\"ignore\")
    pd.set_option(\"display.max_rows\", None, \"display.max_columns\", None)

    while True:

        sdf = input(\"Do you want to keep using the same DataFrame for this session? \").lower()

        if sdf == \"yes\" or sdf == \"y\" or sdf == \"yea\" or sdf == \"ye\" or sdf == \"ya\" or sdf == \"yeah\" or sdf == \"yeh\" or sdf == \"yah\":

            while True:

                useexisting = input(\"Do you want to use an existing DataFrame for this session? \").lower()

                if useexisting == \"yes\" or useexisting == \"y\" or useexisting == \"yea\" or useexisting == \"ye\" or useexisting == \"ya\" or useexisting == \"yeah\" or useexisting == \"yeh\" or useexisting == \"yah\":
                    url = input(\"\\nEnter the name (without the extension) or path of the dataframe that you want to use (or type \\\'quit\\\' to quit): \")+\".csv\"
                    break

                elif useexisting == \"no\" or useexisting == \"n\" or useexisting == \"nay\" or useexisting == \"nah\" or useexisting == \"na\":
                    url = input(\"\\nEnter the download link for the dataframe that you want to use (or type \\\'quit\\\' to quit): \")
                    break

                else:
                    print(\"Invalid choice.\\n\")

            if url == \"q\" or url == \"quit\" or url == \"close\" or url == \"exit\" or url == \"return\":
                print(\"\\nApp Closed.\")
                break

            else:
                print(\"\\nLoading DataFrame...\\n\")
                df = pd.read_csv(url)
                break

        elif sdf == \"no\" or sdf == \"n\" or sdf == \"nay\" or sdf == \"nah\" or sdf == \"na\":
            break

        else:
            print(\"Invalid response.\\n\")

    while True:

        if url == \"q\" or url == \"quit\" or url == \"close\" or url == \"exit\" or url == \"return\":
            break

        if sdf == \"no\" or sdf == \"n\" or sdf == \"nay\" or sdf == \"nah\" or sdf == \"na\":

            while True:

                useexisting = input(\"Do you want to use an existing DataFrame for this session? \").lower()

                if useexisting == \"yes\" or useexisting == \"y\" or useexisting == \"yea\" or useexisting == \"ye\" or useexisting == \"ya\" or useexisting == \"yeah\" or useexisting == \"yeh\" or useexisting == \"yah\":
                    url = input(\"\\nEnter the name (without the extension) or path of the dataframe that you want to use (or type \\\'quit\\\' to quit): \")+\".csv\"
                    break

                elif useexisting == \"no\" or useexisting == \"n\" or useexisting == \"nay\" or useexisting == \"nah\" or useexisting == \"na\":
                    url = input(\"\\nEnter the download link for the dataframe that you want to use (or type \\\'quit\\\' to quit): \")
                    break

                else:
                    print(\"Invalid choice.\\n\")

            if url == \"q\" or url == \"quit\" or url == \"close\" or url == \"exit\" or url == \"return\":
                print(\"\\nApp Closed.\")
                break

            else:
                print(\"\\nLoading DataFrame...\\n\")
                df = pd.read_csv(url)


        action = input(\"\\nWhat do you want to do (type \\\'formats\\\' to view formats that you can use or \\\'quit\\\' to quit)? \").lower()

        fts = [
            \"regular (reg): A regular table view of the DataFrame.\",
            \"information (info): Shows an overview of the contents in the DataFrame.\",
            \"describe (desc): Shows numerical statistics like mean, standard deviation, etc.\",
            \"value counts (vc): Shows the number of times each value appears in a column.\",
            \"prediction model (pred): Creates a prediction model that can predict values based on the data that is given.\",
            \"find value (fv): Shows occurrences of a chosen value and the location(s) of those occurrences.\",
            \"find and replace (fr): Shows occurrences of a chosen value and the location(s) of those occurrences, and allows you to replace them with another value.\",
            \"save as (s): Lets you save the DataFrame as a .csv file.\",
            \"edit/modify: Lets you edit values in the DataFrame.\"
        ]

        if action == \"q\" or action == \"quit\" or action == \"close\" or action == \"exit\" or action == \"return\":
            print(\"\\nApp Closed.\")
            break

        elif action == \"formats\" or action == \"fts\" or action == \"f\":
            print()
            for i in fts:
                print(\" -\", i)

        else:

            if action == \"regular\" or action == \"reg\" or action == \"plain\" or action == \"df\" or action == \"dataframe\" or action == \"table\":

                column = input(\"Enter the column you want to search for in here (type \\\'all\\\' to view all columns or \\\'multi\\\' to view multiple columns): \").lower()

                if column == \"all\":
                    s = int(input(\"Enter the starting row number for your selection: \"))
                    e = int(input(\"Enter the ending row number for your selection: \")) + 1
                    print(f\"\\n{df[s:e]}\")

                elif column == \"multi\" or column == \"multiple\":

                    cnum = int(input(\"How many columns do you want to select? \"))
                    cols = []

                    for i in range(cnum):
                        col = input(f\"Column {i + 1}: \")
                        if col in df.columns:
                            cols.append(col)
                        else:
                            print(f\"The \\\'{col}\\\' column is not in this DataFrame.\\n\")
                            break

                    if len(cols) == cnum:
                        s = int(input(\"Enter the starting row number for your selection: \"))
                        e = int(input(\"Enter the ending row number for your selection: \")) - 1

                        print(f\"\\n{df.loc[s:e, cols]}\")

                    else:
                        pass

                else:

                    if column in df.columns:
                        s = int(input(\"Enter the starting row number for your selection: \"))
                        e = int(input(\"Enter the ending row number for your selection: \")) - 1
                        print(f\"\\n{df.loc[s:e, column]}\")
                    else:
                        print(\"Invalid column. Please try again.\")

            elif action == \"info\" or action == \"information\":
                print(df.info())

            elif action == \"desc\" or action == \"describe\" or action == \"description\":
                print(df.describe())

            elif action == \"value counts\" or action == \"vc\" or action == \"value_counts\":
                column = input(\"Enter the column you want to search for in here: \").lower()
                if column in df.columns:
                    print(df[column].value_counts())
                else:
                    print(\"Invalid column. Please try again.\")

            elif action == \"pred\" or action == \"prediction\" or action == \"predict\" or action == \"predict value\" or action == \"p\" or action == \"prediction model\":

                cnum = input(\"How many columns do you want to use as feature (x axis) variables (type \\\'auto\\\' to automatically select the best columns for prediction)? \").lower()
                s = input(\"Enter the starting row number for your selection (type \\\'all\\\' to select all rows - this is more accurate but will result in a large predicted output): \")

                if s == \"all\" or s == \"everything\":
                    s = 0
                    e = df.shape[0]

                else:
                    e = int(input(\"Enter the ending row number for your selection: \")) + 1

                if cnum == \"auto\" or cnum == \"automatic\":

                    predcol = input(\"What column do you want to predict? \")
                    t = df.loc[s:e, predcol]

                    print(\"\\nCreating model...\\n\")

                    cols = []

                    for i in range(len(df.corr()[predcol])):
                        if df.corr()[predcol][i] >= 0.5:
                            cols.append(df.corr()[predcol].index[i])

                else:

                    cnum = int(cnum)
                    cols = [input(f\"Column {i+1}: \") for i in range(cnum)]
                    t = df[input(\"What column do you want to predict? \")]

                    print(\"\\nCreating model...\\n\")

                for x in df.columns:

                    if type(df[x][0]) != int and type(df[x][0]) != float:
                        dfd = pd.get_dummies(df[x], dtype=int)
                        df.drop(columns=[x])

                        for y in dfd.columns:
                            df[y] = dfd[y]

                f = df.loc[s:e, cols]

                xtrain, xtest, ytrain, ytest = tts(f, t, test_size=0.3, random_state=20)
                lr = lreg().fit(xtrain, ytrain)
                pred = lr.predict(xtest)

                print(f\"Mean of Predicted Values: {pred.mean()}\\n\\nModel Accuracy: {lr.score(xtest, ytest)*100}%.\")

                view = input(\"Would you like to view a list of the predicted values? \").lower()

                if view == \"yes\" or view == \"y\" or view == \"ye\" or view == \"ya\" or view == \"yep\" or view == \"yeah\" or view == \"yea\" or view == \"yah\":
                    print(\"\\nPredicted Values:\\n\")
                    for i in pred:
                        print(f\" - {i}\")

            elif action == \"find\" or action == \"search\" or action == \"value search\" or action == \"find value\" or action == \"vs\" or action == \"fv\":

                cnum = input(\"How many columns do you want to use (type \\\'all\\\' for all columns)? \")

                if cnum == \"all\":
                    cols = [i for i in df.columns]
                else:
                    cnum = int(cnum)
                    cols = []

                    for i in range(cnum):
                        col = input(f\"Column {i + 1}: \")
                        if col in df.columns:
                            cols.append(col)
                        else:
                            print(f\"The \\\'{col}\\\' column is not in this DataFrame.\\n\")
                            break


                value = input(\"What value do you want to search for? \").lower()
                view = input(\"Do you want to view the occurences of this value (y/n)? \").lower()

                for x in cols:

                    print(f\"\\n\\\'{x}\\\' Column:\\n\")
                    count = 0

                    for y in df[x]:
                        if str(y).lower() == value:
                            count += 1

                    print(f\"Found {count} occurences of {value}.\\n\")

                    if view == \"yes\" or view == \"y\" or view == \"ye\" or view == \"yeah\" or view == \"ya\" or view == \"yep\" or view == \"yea\" or view == \"yah\" or view == \"yeh\":

                        print(\"Occurences:\\n\")

                        for z in range(len(df[x])):
                            if str(df[x][z]).lower() == value:
                                print(f\" - Row {z+1}\")

            elif action == \"find and replace\" or action == \"fr\" or action == \"replace\" or action == \"rep\":

                print(\"\\nDisclaimer: DataFrame modifications will only be applied in the current session.\\n\")

                value = input(\"What value do you want to search for? \").lower()
                rep = input(\"What value do you want to replace it with? \")
                view = input(\"Do you want to view the occurences of this value (y/n)? \").lower()

                for x in df.columns:

                    print(f\"\\n\\\'{x}\\\' Column:\\n\")
                    count = 0
                    lst = []

                    for y in df[x]:
                        if str(y).lower() == value:
                            count += 1

                    if count == 0:
                        print(f\"Could not find occurences of {value}.\\n\")

                    else:

                        if view == \"yes\" or view == \"y\" or view == \"ye\" or view == \"yeah\" or view == \"ya\" or view == \"yep\" or view == \"yea\" or view == \"yah\" or view == \"yeh\":

                            print(\"Occurences:\\n\")

                            for o in range(len(df[x])):
                                if str(df[x][y]).lower() == value:
                                    print(f\" - Row {o+1}\")

                        print(f\"Found {count} occurences of {value}.\\n\")

                        replace = input(f\"\\nDo you want to replace the occurences of \\\'{value}\\\' in the \\\'{x}\\\' column (y/n)? \").lower()

                        if replace == \"yes\" or replace == \"y\" or replace == \"ye\" or replace == \"yeah\" or replace == \"ya\" or replace == \"yep\" or replace == \"yea\" or replace == \"yah\" or replace == \"yeh\":

                            for i in df[x]:

                                if str(df[x][y]).lower() == str(value).lower():
                                    lst.append(rep)

                                else:
                                    lst.append(str(df[x][y]).lower())

                            df.drop(columns=[x])
                            df[x] = pd.Series(lst)
            
            elif action == \"save\" or action == \"save as\" or action == \"s\":

                print(\"\\nNote: Console must be shut down for file(s) to be saved.\\n\")

                loc = input(\"What do you want to name your saved file? \")
                loc = loc+\".csv"

                df.to_csv(loc)
                print(f"Successfully saved file as {loc}.")


            elif action == "edit" or action == "modify":

                col = input("\\nWhat column do you want to edit? ")
                lst = list(df[col])

                print(f"\\n\\nEditing {col}:\\n\")

                while True:

                    row = input(\"\\nWhat row do you want to edit (type \\\'return\\\' to go back)? \")

                    if row == \"q\" or row == \"quit\" or row == \"close\" or row == \"exit\" or row == \"return\" or row == \"back\":
                        break

                    else:

                        row = int(row)-1

                        print(f\"\\nCurrent Value: {lst[row]}\")

                        value = input(\"New value: \")

                        try:
                            value = float(value)
                        except:
                            value = str(value)

                        lst[row] = value

                df.drop(columns=[col])
                df[col] = pd.Series(lst)
            
            else:
                print(\"Invalid choice. Please try again.\\n\")
"""
    fm = """
def fm():

    print(\"-\"*23+\"\\nFile Creator and Editor\\n\"+\"-\"*23)
    print(\"\\n(Note: Shut down the console to apply changes)\")

    import os

    while True:

        action = str(input(\"\\nEnter what you want to do here (\\\'write\\\' - rewrites the file, \\\'read\\\' - lets you read the file, \\\'delete\\\' to delete a file, \\\'mf\\\' to make a folder, \\\'move\\\' to move a file or \\\'quit\\\' to quit the software): \")).lower()

        if action == \"q\" or action == \"quit\" or action == \"close\" or action == \"exit\":
            print(\"\\nApp Closed.\")
            break

        else:

            if action == \"write\" or action == \"w\":

                name = str(input(\"Enter the name of the file with the extension (\\\'.txt\\\', \\\'.py\\\', etc.): \"))

                file = open(name, \"w\")

                print(\"\\n(Type \\\'/q/\\\' to exit the editor)\\n\\n\")

                line = 1

                text = input(f\"Line {line}: \")
                line += 1

                if text != \"/q/\":

                    write = text

                    while True:

                        if text == \"/q/\":
                            break

                        else:

                            text = input(f\"Line {line}: \")
                            write = write+\"\\n\"+text
                            line += 1

                    file.write(write)

                print(name, \"was rewritten successfully.\")

            elif action == \"del\" or action == \"delete\" or action == \"d\":
                file = str(input(\"Enter the name of the file that you want to delete with its extension (\\\'.txt\\\', \\\'.py\\\', etc.): \"))
                os.remove(file)
                print(f\"{file} deleted successfully.\")

            elif action == \"read\" or action == \"r\":
                name = str(input(\"Enter the name of the file with the extension (\\\'.txt\\\', \\\'.py\\\', etc.): \"))
                file = open(name, \"r\")
                read = file.read()
                print(f\"\\n{\'-\'*200}\\n{read}\\n{\'-\'*200}\\n\")

            elif action == \"move\" or action == \"mv\":

                name = str(input(\"Enter the name of the file with the extension (\\\'.txt\\\', \\\'.py\\\', etc.): \"))
                folder = input(\"What folder do you want to move this file to (type \\\'/q/\\\' to go back)? \")

                if folder != \"/q/\":

                    os.system(f\"mv {name} {folder}\\\\{name}\")

            elif action == \"mkdir\" or action == \"make directory\" or action == \"make folder\" or action == \"mf\" or action == \"mkf\" or action == \"create folder\" or action == \"create directory\":

                print(\"\\n(Note: Folder name cannot contain any of the following characters: \\\'/\\\', \\\'\\\\\\\', \\\'?\\\', \\\':\\\', \\\'|\\\', \\\'<\\\', \\\'>\\\', \\\'*\\\', \\\'\\\"\\\'. Also, an existing folder cannot be recreated, as this will crash the app.)\\n\")

                name = input(\"What do you want to name your folder (type \'/q/\' to go back)? \")

                if name != \"/q/\":
                    os.mkdir(name)

            else:
                print(\"Invalid option. Please try again.\")
"""
    gtn = """
def gtn():

    import random

    print(\"\\n\\nGuess The Number\")

    global rounds
    rounds = 0
    rounds -= 1
    wins = 0
    losses = 0
    errors = 0

    while True:

        rounds += 1


        print(\"\\nRounds played:\", rounds, \"\\n\")
        print(\"Wins:\", wins)
        print(\"Losses:\", losses)
        print(\"Errors:\", errors)

        mode = input(\"\\nEnter difficulty here (\\\'Easy\\\', \\\'Medium\\\', \\\'Hard\\\', \\\'Insane\\\', \\\'Impossible\\\', \\\'ImpossibleX\\\' or \\\'quit\\\' to quit): \")

        if mode == \"quit\" or mode == \"q\" or mode == \"exit\" or mode == \"close\":
            print(\"\\nApp Closed.\")
            break

        elif mode == \"Easy\" or mode == \"easy\" or mode == \"ez\" or mode == \"e\" or mode == \"E\" or mode == \"EZ\":
            num = int(random.randint(0, 10))
            print(\"I am thinking of a number between 1 and 10. What is it?\")
            answer = int(input(\"Enter your guess here: \"))

            if answer == num:
                print(\"\\nYou win! Next round, coming up!\")
                wins += 1

            elif answer > num:
                print(\"\\nToo high! You lost. Try again in the next round!\")
                losses += 1
            elif answer < num:
                print(\"\\nToo low! You lost. Try again in the next round!\")
                losses += 1

        elif mode == \"Medium\" or mode == \"medium\" or mode == \"med\" or mode == \"Med\" or mode == \"mid\" or mode == \"Mid\" or mode == \"M\" or mode == \"m\":
            num = int(random.randint(0, 100))
            print(\"I am thinking of a number between 1 and 100. What is it?")
            answer = int(input(\"Enter your guess here: \"))

            if answer == num:
                print(\"\\nYou win! Next round, coming up!\")
                wins += 1

            elif answer > num:
                print(\"\\nToo high! You lost. Try again in the next round!\")
                losses += 1
            elif answer < num:
                print(\"\\nToo low! You lost. Try again in the next round!\")
                losses += 1


        elif mode == \"Hard\" or mode == \"hard\" or mode == \"h\" or mode == \"H":
            num = int(random.randint(0, 1000))
            print(\"I am thinking of a number between 1 and 1000. What is it?\")
            answer = int(input("Enter your guess here: \"))

            if answer == num:
                print(\"\\nYou win! Next round, coming up!\")
                wins += 1

            elif answer > num:
                print(\"\\nToo high! You lost. Try again in the next round!\")
                losses += 1
            elif answer < num:
                print(\"\\nToo low! You lost. Try again in the next round!\")
                losses += 1


        elif mode == \"Insane\" or mode == \"insane\" or mode == \"in\" or mode == \"In\":
            num = int(random.randint(0, 10000))
            print(\"I am thinking of a number between 1 and 10 000. What is it?\")
            answer = int(input(\"Enter your guess here: \"))

            if answer == num:
                print(\"\\nYou win! Next round, coming up!\")
                wins += 1

            elif answer > num:
                print(\"\\nToo high! You lost. Try again in the next round!\")
                losses += 1
            elif answer < num:
                print(\"\\nToo low! You lost. Try again in the next round!\")
                losses += 1
            else:
                print(\"\\nThat wasn't a valid answer. Please enter a valid answer in the next round.\")
                errors += 1

        elif mode == \"Impossible\" or mode == \"impossible\" or mode == \"im\" or mode == \"Im\":
            num = int(random.randint(0, 100000))
            print(\"I am thinking of a number between 1 and 100 000. What is it?\")
            answer = int(input(\"Enter your guess here: \"))

            if answer == num:
                print(\"\\nYou win! Next round, coming up!")
                wins += 1

            elif answer > num:
                print(\"\\nToo high! You lost. Try again in the next round!\")
                losses += 1
            elif answer < num:
                print(\"\\nToo low! You lost. Try again in the next round!\")
                losses += 1

        elif mode == \"ImpossibleX\" or mode == \"impossibleX\" or mode == \"imx\" or mode == \"Imx\" or mode == \"Impossiblex\" or mode == \"impossiblex\" or mode == \"ImX\" or mode == \"imX\":
            num = int(random.randint(0, 1000000))
            print(\"I am thinking of a number between 1 and 1 000 000. What is it?\")
            answer = int(input(\"Enter your guess here: \"))

            if answer == num:
                print(\"\\nYou win! Next round, coming up!\")
                wins += 1

            elif answer > num:
                print(\"\\nToo high! You lost. Try again in the next round!\")
                losses += 1
            elif answer < num:
                print(\"\\nToo low! You lost. Try again in the next round!\")
                losses += 1

        else:
            print(\"\\nThere was an error.\")
            errors += 1
"""
    mcc = """
def mcc():
    def mte(s):

        l = []
        e = \"\"
        y = \"\"

        s.append(\" \")
        s.append(\"/\")

        for x in s:

            if x == \"/\":
                l.append(\" \")

            elif x == \" \":

                if y == \".-\" or y == \"*-\":
                    l.append(\"A\")

                elif y == \"-...\" or y == \"-***\":
                    l.append(\"B\")

                elif y == \"-.-.\" or y == \"-*-*\":
                    l.append(\"C\")

                elif y == \"-..\" or y == \"-**\":
                    l.append(\"D\")

                elif y == \".\" or y == \"*\":
                    l.append(\"E\")

                elif y == \"..-.\" or y == \"**-*\":
                    l.append(\"F\")

                elif y == \"--.\" or y == \"--*\":
                    l.append(\"G\")

                elif y == \"....\" or y == \"****\":
                    l.append(\"H\")

                elif y == \"..\" or y == \"**\":
                    l.append(\"I\")

                elif y == \".---\" or y == \"*---\":
                    l.append("J")

                elif y == \"-.-\" or y == \"-*-\":
                    l.append(\"K\")

                elif y == \".-..\" or y == \"*-**\":
                    l.append(\"L\")

                elif y == \"--\":
                    l.append(\"M\")

                elif y == \"-.\" or y == \"-*\":
                    l.append(\"N\")

                elif y == \"---\":
                    l.append(\"O\")

                elif y == \".--.\" or y == \"*--*\":
                    l.append(\"P\")

                elif y == \"--.-\" or y == \"--*-\":
                    l.append(\"Q\")

                elif y == \".-.\" or y == \"*-*\":
                    l.append(\"R\")

                elif y == \"...\" or y == \"***\":
                    l.append(\"S\")

                elif y == \"-\":
                    l.append(\"T\")

                elif y == \"..-\" or y == \"**-\":
                    l.append(\"U\")

                elif y == \"...-\" or y == \"***-\":
                    l.append(\"V\")

                elif y == \".--\" or y == \"*--\":
                    l.append(\"W\")

                elif y == \"-..-\" or y == \"-**\":
                    l.append(\"X\")

                elif y == \"-.--\" or y == \"-*--\":
                    l.append(\"Y\")

                elif y == \"--..\" or y == \"--**\":
                    l.append(\"Z\")

                elif y == \"-----\":
                    l.append(\"0\")

                elif y == \".----\" or y == \"*----\":
                    l.append(\"1\")

                elif y == \"..---\" or y == \"**---\":
                    l.append(\"2\")

                elif y == \"...--\" or y == \"***--\":
                    l.append(\"3\")

                elif y == \"....-\" or y == \"****-\":
                    l.append(\"4\")

                elif y == \".....\" or y == \"*****\":
                    l.append(\"5\")

                elif y == \"-....\" or y == \"-****\":
                    l.append(\"6\")

                elif y == \"--...\" or y == \"--***\":
                    l.append(\"7\")

                elif y == \"---..\" or y == \"---**\":
                    l.append(\"8\")

                elif y == \"----.\" or y == \"----*\":
                    l.append(\"9\")

                elif y == \".-.-.-\"  or y == \"*-*-*-\":
                    l.append(\".\")

                elif y == \"--..--\" or y == \"--**--\":
                    l.append(\",\")

                elif y == \"---...\" or y == \"---***\":
                    l.append(\":\")

                elif y == \"..--..\" or y == \"**--**\":
                    l.append(\"?\")

                elif y == \".----.\" or y == \"*----*\":
                    l.append(\"\\\'\")

                elif y == \"-....-\" or y == \"-****-\":
                    l.append(\"-\")

                elif y == \".-..-.\" or y == \"*-**-*\":
                    l.append(\"\\\"\")

                elif y == \"-.-.--\" or y == \"-*-*--\":
                    l.append(\"!\")

                y = \"\"

            else:
                y = y+x

        for i in l:
            e = e+str(i)

        print(e)

    def etm(s):

            l = []
            m = \"\"

            for x in s:

                if x == \"A\" or x == \"a\":
                    l.append(\".-\")

                elif x == \"B\" or x == \"b\":
                    l.append(\"-...\")

                elif x == \"C\" or x == \"c\":
                    l.append(\"-.-.\")

                elif x == \"D\" or x == \"d\":
                    l.append(\"-..\")

                elif x == \"E\" or x == \"e\":
                    l.append(\".\")

                elif x == \"F\" or x == \"f\":
                    l.append(\"..-.\")

                elif x == \"G\" or x == \"g\":
                    l.append(\"--.\")

                elif x == \"H\" or x == \"h\":
                    l.append(\"....\")

                elif x == \"I\" or x == \"i\":
                    l.append(\"..\")

                elif x == \"J\" or x == \"j\":
                    l.append(\".---\")

                elif x == \"K\" or x == \"k\":
                    l.append(\"-.-\")

                elif x == \"L\" or x == \"l\":
                    l.append(\".-..\")

                elif x == \"M\" or x == \"m\":
                    l.append(\"--\")

                elif x == \"N\" or x == \"n\":
                    l.append(\"-.\")

                elif x == \"O\" or x == \"o\":
                    l.append(\"---\")

                elif x == \"P\" or x == \"p\":
                    l.append(\".--.\")

                elif x == \"Q\" or x == \"q\":
                    l.append(\"--.-\")

                elif x == \"R\" or x == \"r\":
                    l.append(\".-.\")

                elif x == \"S\" or x == \"s\":
                    l.append(\"...\")

                elif x == \"T\" or x == \"t\":
                    l.append(\"-\")

                elif x == \"U\" or x == \"u\":
                    l.append(\"..-\")

                elif x == \"V\" or x == \"v\":
                    l.append(\"...-\")

                elif x == \"W\" or x == \"w\":
                    l.append(\".--\")

                elif x == \"X\" or x == \"x\":
                    l.append(\"-..-\")

                elif x == \"Y\" or x == \"y\":
                    l.append(\"-.--\")

                elif x == \"Z\" or x == \"z\":
                    l.append(\"--..\")

                elif x == \"0\":
                    l.append(\"-----\")

                elif x == \"1\":
                    l.append(\".----\")

                elif x == \"2\":
                    l.append(\"..---\")

                elif x == \"3\":
                    l.append(\"...--\")

                elif x == \"4\":
                    l.append(\"....-\")

                elif x == \"5\":
                    l.append(\".....\")

                elif x == \"6\":
                    l.append(\"-....\")

                elif x == \"7\":
                    l.append(\"--...\")

                elif x == \"8\":
                    l.append(\"---..\")

                elif x == \"9\":
                    l.append(\"----.\")

                elif x == \".\":
                    l.append(\".-.-.-\")

                elif x == \",\":
                    l.append(\"--..--\")

                elif x == \":\":
                    l.append(\"---...\")

                elif x == \"?\":
                    l.append(\"..--..\")

                elif x == \"\\\'\":
                    l.append(\".----.\")

                elif x == \"-\":
                    l.append(\"-....-\")

                elif x == \"\\\"\":
                    l.append(\".-..-.\")

                elif x == \"!\":
                    l.append(\"-.-.--\")
                elif x == \" \":
                    l.append(\"/\")

                else:
                    print(x, \"is an invalid character.\")

            m = m + l[0]

            for y in l[1:]:
                m = m + \" \" + y

            print(m)


    while True:

        cm = input(\"\\nEnter m-e for Morse to English, e-m for English to Morse or \\\'quit\\\' to quit: \")

        if cm == \'q\' or cm == \"quit\" or cm == \"close\":
            print(\"\\nApp Closed.\")
            break

        elif cm == \"e-m\" or cm == \"etm\":
            ui = list(input(\"Enter the message you want to convert to morse here: \"))
            etm(ui)

        elif cm == \"m-e\" or cm == \"mte\":
            ui = list(input(\"Enter the message you want to convert to english here (letters with a space between them and words with \\\" / \\\" between them): \"))
            mte(ui)

        else:
            print(\"Invalid input. Please try again.\")
"""
    rng = """
def rng():

    while True:

        import random

        digits = input(\"\\nEnter the amount of digits you want to use - the number may take a bit to load if it has more than 100 000 digits (enter \\\'quit\\\' to quit): \")

        if digits == \"quit\" or digits == \"q\" or digits == \"close\" or digits == \"exit\":
            print(\"\\nApp Closed.\")
            break

        else:

            digits = int(digits)

            if digits == 1:
                print(\"Here is your number:\", random.randint(0, 9))
            else:
                power1 = digits-1
                power2 = 10**digits
                numpar1 = 10**power1
                numpar2 = power2-1
                num = random.randint(numpar1, numpar2)
                print(\"Here is your number:\", num)"""
    rpg = """
def rpg():

    while True:

        import random as r

        global password

        chars = input(\"\\nEnter the length of the password here (or type \\\'quit\\\' to quit): \")
        randInt = r.randint(0, 87)
        password = []
        pstr = \"\"


        def charAppend(pwd, num):

            if num == 10:
                pwd.append(\"A\")
            elif num == 11:
                pwd.append(\"B\")
            elif num == 12:
                pwd.append(\"C\")
            elif num == 13:
                pwd.append(\"D\")
            elif num == 14:
                pwd.append(\"E\")
            elif num == 15:
                pwd.append(\"F\")
            elif num == 16:
                pwd.append(\"G\")
            elif num == 17:
                pwd.append(\"H\")
            elif num == 18:
                pwd.append(\"I\")
            elif num == 19:
                pwd.append(\"J\")
            elif num == 20:
                pwd.append(\"K\")
            elif num == 21:
                pwd.append(\"L\")
            elif num == 22:
                pwd.append(\"M\")
            elif num == 23:
                pwd.append(\"N\")
            elif num == 24:
                pwd.append(\"O\")
            elif num == 25:
                pwd.append(\"P\")
            elif num == 26:
                pwd.append(\"Q\")
            elif num == 27:
                pwd.append(\"R\")
            elif num == 28:
                pwd.append(\"S\")
            elif num == 29:
                pwd.append(\"T\")
            elif num == 30:
                pwd.append(\"U\")
            elif num == 31:
                pwd.append(\"V\")
            elif num == 32:
                pwd.append(\"W\")
            elif num == 33:
                pwd.append(\"X\")
            elif num == 34:
                pwd.append(\"Y\")
            elif num == 35:
                pwd.append(\"Z\")
            elif num == 36:
                pwd.append(\"!\")
            elif num == 37:
                pwd.append(\"@\")
            elif num == 38:
                pwd.append(\"#\")
            elif num == 39:
                pwd.append(\"$\")
            elif num == 40:
                pwd.append(\"%\")
            elif num == 41:
                pwd.append(\"^\")
            elif num == 42:
                pwd.append(\"&\")
            elif num == 43:
                pwd.append(\"*\")
            elif num == 44:
                pwd.append(\"(\")
            elif num == 45:
                pwd.append(\")\")
            elif num == 46:
                pwd.append(\"-\")
            elif num == 47:
                pwd.append(\"_\")
            elif num == 48:
                pwd.append(\"+\")
            elif num == 49:
                pwd.append(\"=\")
            elif num == 50:
                pwd.append(\";\")
            elif num == 51:
                pwd.append(\":\")
            elif num == 52:
                pwd.append(\"[\")
            elif num == 53:
                pwd.append(\"]\")
            elif num == 54:
                pwd.append(\"{\")
            elif num == 55:
                pwd.append(\"}\")
            elif num == 56:
                pwd.append(\"\\\\\")
            elif num == 57:
                pwd.append(\"|\")
            elif num == 58:
                pwd.append(\"<\")
            elif num == 59:
                pwd.append(\">\")
            elif num == 60:
                pwd.append(\"/\")
            elif num == 61:
                pwd.append(\"?\")
            elif num == 62:
                pwd.append(\"a\")
            elif num == 63:
                pwd.append(\"b\")
            elif num == 64:
                pwd.append(\"c\")
            elif num == 65:
                pwd.append(\"d\")
            elif num == 66:
                pwd.append(\"e\")
            elif num == 67:
                pwd.append(\"f\")
            elif num == 68:
                pwd.append(\"g\")
            elif num == 69:
                pwd.append(\"h\")
            elif num == 70:
                pwd.append(\"i\")
            elif num == 71:
                pwd.append(\"j\")
            elif num == 72:
                pwd.append(\"k\")
            elif num == 73:
                pwd.append(\"l\")
            elif num == 74:
                pwd.append(\"m\")
            elif num == 75:
                pwd.append(\"n\")
            elif num == 76:
                pwd.append(\"o\")
            elif num == 77:
                pwd.append(\"p\")
            elif num == 78:
                pwd.append(\"q\")
            elif num == 79:
                pwd.append(\"r\")
            elif num == 80:
                pwd.append(\"s\")
            elif num == 81:
                pwd.append(\"t\")
            elif num == 82:
                pwd.append(\"u\")
            elif num == 83:
                pwd.append(\"v\")
            elif num == 84:
                pwd.append(\"w\")
            elif num == 85:
                pwd.append(\"x\")
            elif num == 86:
                pwd.append(\"y\")
            elif num == 87:
                pwd.append(\"z\")


        if chars == \"q\" or chars == \"quit\" or chars == \"exit\" or chars == \"close\":
            print(\"\\nApp closed.\")
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


            print(\"Here is your password:\", pstr)
"""
    rps = """
hist = []
choices = [\"Rock\", \"Paper\", \"Scissors\"]
wins = 0
losses = 0
ivd = 0
rnds = 1

def rps():

    print(\"\\n\\n\"+\"-\"*len(\"Rock, Paper Scissors\")+\"\\nRock, Paper Scissors\\n\"+\"-\"*len(\"Rock, Paper Scissors\"))

    global wins, losses, ivd, rnds, choices

    def check():

        global wins, losses, ivd, rnds, choices

        if com == user:

            print(\"Tie! Both of us chose\", choices[com] + "!")

        else:


            if user == 0 and com == 1:
                print(\"You lost! You chose\", choices[user], \"and I chose\", choices[com], end=\".\\n\")
                losses += 1

            elif user == 0 and com == 2:
                print(\"You won! You chose\", choices[user], \"and I chose\", choices[com], end=\".\\n")
                wins += 1

            elif user == 1 and com == 0:
                print(\"You won! You chose\", choices[user], \"and I chose\", choices[com], end=\".\\n\")
                wins += 1

            elif user == 1 and com == 2:
                print(\"You lost! You chose\", choices[user], \"and I chose\", choices[com], end=\".\\n\")
                losses += 1

            elif user == 2 and com == 0:
                print(\"You lost! You chose\", choices[user], \"and I chose\", choices[com], end=\".\\n\")
                losses += 1

            elif user == 2 and com == 1:
                print(\"You won! You chose\", choices[user], \"and I chose\", choices[com], end=\".\\n\")
                wins += 1

    while True:

        print(\"\\nRound:\", rnds)
        print(\"Score:\", str(wins) + \"-\" + str(losses), \"(you-me)\")
        print(\"Invalid Rounds:\", ivd)

        import random as rnd


        ui = input(\"\\n\\nRock, Paper, or Scissors (type \\\'quit\\\' to quit or \\\'history\\\' to check the current game's history)? \")
        com = rnd.randint(0, 2)


        if ui == \"q\" or ui == \"quit\" or ui == \"exit\" or ui == \"close\":

            print(\"Good Game!\", \"The score is\", str(wins)+\"-\"+str(losses), \"(you-me).\")
            print(\"\\nApp Closed.\")
            break

        elif ui == \"history\" or ui == \"h\" or ui == \"hist\" or ui == \"recent\":

            print(\"\\nGame History (you-me):\\n\")

            if hist == []:
                print(\"Play a round to add it to the history!\\n\\n\")

            else:
                for h in hist:
                    print(h)

        else:

            if ui == \"Rock\" or ui == \"r\\" or ui == \"rock\" or ui == \"R\" or ui == 1:
                user = 0
                check()

            elif ui == \"Paper\" or ui == \"p\" or ui == \"paper\" or ui == \"P\" or ui == 2:
                user = 1
                check()

            elif ui == \"Scissors\" or ui == \"s\" or ui == \"scissors\" or ui == \"S\" or ui == 3:
                user = 2
                check()

            else:
                print(\"\\nInvalid Choice. Please try again.\")
                ivd += 1

            rnds += 1
            rhist = \"Round \"+str(rnds)+\": \"+ui+\" VS \"+choices[com]+\": \"+str(wins)+\"-\"+str(losses)
            hist.append(rhist)
"""
    settings = """
dtf = \"%B, %d %Y\"
tf = \"%I:%M:%S %p\"

user = None
pw = None
name = None

hcl = None

def settings():

    import settingsource as src

    global dtf, tf
    global user, pw, name
    global hcl

    print(\"\\n\" + \"-\" * len(\"AarOS Settings\") + \"\\nAarOS Settings\\n\" + \"-\" * len(\"AarOS Settings\"))
    print(\"Note: Console must be shut down for changes to take effect.\\n\")

    if src.dtf != \"\":
        dtf = src.dtf
    else:
        dtf = \"%B, %d %Y\"

    if src.tf != \"\":
        tf = src.tf
    else:
        tf = \"%I:%M:%S %p\"

    user = src.username
    pw = src.password
    name = src.name

    hcl = src.hcl

    def dt():

        global dtf
        global tf

        while True:

            mfts = [\"\\\'short\\\' - Shortened version of the month name\", \"\\\'full\\\' - Full month name\", \"\\\'num\\\' - Month number\"]
            dt = input(\"\nWould you like to change settings for date or time (\\\'date\\\' for date, \\\'time\\\' for time or \\\'back\\\' to go back)? \").lower()

            if dt == \"return\" or dt == \"r\" or dt == \"back\" or dt == \"b\" or dt == \"exit\" or dt == \"close\" or dt == \"q\" or dt == \"quit\":
                break

            elif dt == \"date\" or dt == \"dt\" or dt == \"d\":

                dtf = \"\"

                while True:

                    e1 = input(\"What element do you want to appear first (Month, Day or Year)? \").lower()

                    if e1 == \"month\" or e1 == \"m\":

                        while True:

                            mf = input(\"\\nWhat month format do you want to use (type \\\'formats\\\' for a list of month formats that you can use)? \").lower()

                            if mf == \"formats\" or mf == \"fts\":
                                print()
                                for i in mfts:
                                    print(\" - \"+i)

                            if mf == \"short\" or mf == \"s\" or mf == \"shortened\":
                                e1 = \"%b\"
                                break

                            elif mf == \"long\" or mf == \"l\" or mf == \"full\" or mf == \"f\":
                                e1 = \"%B\"
                                break

                            elif mf == \"num\" or mf == \"numerical\" or mf == \"number\":
                                e1 = \"%m\"
                                break

                        break

                    elif e1 == \"day\" or e1 == \"d\":
                        e1 = \"%d\"
                        break

                    elif e1 == \"year\" or e1 == \"y\":
                        e1 = \"%Y\"
                        break

                    else:
                        print(\"Invalid input. Please try again.\")

                while True:

                    e2 = input(\"What element do you want to appear second (Month, Day or Year)? \").lower()

                    if e2 == \"month\" or e2 == \"m\":

                        while True:

                            mf = input(\"\\nWhat month format do you want to use (type \\\'formats\\\' for a list of month formats that you can use)? \").lower()

                            if mf == \"formats\" or mf == \"fts\":
                                print()
                                for i in mfts:
                                    print(\" - \" + i)

                            if mf == \"short\" or mf == \"s\" or mf == \"shortened\":
                                e2 = \"%b\"
                                break

                            elif mf == \"long\" or mf == \"l\" or mf == \"full\" or mf == \"f\":
                                e2 = \"%B\"
                                break

                            elif mf == \"num\" or mf == \"numerical\" or mf == \"number\":
                                e2 = \"%m\"
                                break

                        break

                    elif e2 == \"day\" or e2 == \"d\":
                        e2 = \"%d\"
                        break

                    elif e2 == \"year\" or e2 == \"y\":
                        e2 = e2 + \"%Y\"
                        break

                    else:
                        print(\"Invalid format. Please try again.\")
                        f = input(\"What order of elements do you want to use (separate using a \\\'/\\\' eg. MM/DD/YYYY)? \").upper()

                while True:

                    e3 = input(\"What element do you want to appear last (Month, Day or Year)? \").lower()

                    if e3 == \"month\" or e3 == \"m\":

                        while True:

                            mf = input(\"\\nWhat month format do you want to use (type \\\'formats\\\' for a list of month formats that you can use)? \").lower()

                            if mf == \"formats\" or mf == \"fts\":
                                print()
                                for i in mfts:
                                    print(\" - \" + i)

                            if mf == \"short\" or mf == \"s\" or mf == \"shortened\":
                                e3 = \"%b\"
                                break

                            elif mf == \"long\" or mf == \"l\" or mf == \"full\" or mf == \"f\":
                                e3 = \"%B\"
                                break

                            elif mf == \"num\" or mf == \"numerical\" or mf == \"number\":
                                e3 = \"%m\"
                                break

                        break

                    elif e3 == \"day\" or e3 == \"d\":
                        e3 = \"%d\"
                        break

                    elif e3 == \"year\" or e3 == \"y\":
                        e3 = \"%Y\"
                        break

                    else:
                        print(\"Invalid format. Please try again.\")


                while True:

                    s = input(\"What separator do you want to use for the date (\\\',\\\' or \\\'/\\\')? \")

                    if s == \",\":
                        dtf = e1+\", \"+e2+\" \"+e3
                        break

                    elif s == \"/\":
                        dtf = e1+\"/\"+e2+\"/\"+e3
                        break

                    else:
                        print(\"Invalid separator. Please try again.\")

            elif dt == \"time\" or dt == \"t\":

                tf = \"\"

                while True:

                    f = input(\"Do you want to use 24H or 12H time format? \").upper()

                    if f == \"12H\" or f == \"12 HOUR\" or f == \"12HR\" or f == \"12 HR\":
                        tf = tf+\"%I:%M\"
                        break

                    elif f == \"24H\" or f == \"24 HOUR\" or f == \"24HR\" or f == \"24 HR\":
                        tf = tf+\"%H:%M\"
                        break

                    else:
                        print(\"Invalid format. Please try again.\")

                while True:

                    s = input(\"Seconds (On/Off): \").lower()

                    if s == \"on\" or s == \"true\" or s == \"yes\" or s == \"y\":

                        tf = tf+\":%S\"

                        while True:

                            ms = input(\"Milliseconds (On/Off): \").lower()

                            if ms == \"on\" or ms == \"true\" or ms == \"yes\" or ms == \"y\":
                                tf = tf + \".%f\"
                                break
                            elif ms == \"off\" or ms == \"false\" or ms == \"no\" or ms == \"n\":
                                break
                            else:
                                print(\"Invalid choice. Please try again.\\n\")

                        break

                    elif s == \"off\" or s == \"false\" or s == \"no\" or s == \"n\":
                        break
                    else:
                        print(\"Invalid choice. Please try again.\\n\")

                while True:

                    h = input(\"AM/PM (On/Off): \").lower()

                    if h == \"on\" or h == \"true\" or h == \"yes\" or h == \"y\":
                        tf = tf + \" %p\"
                        break
                    elif h == \"off\" or h == \"false\" or h == \"no\" or h == \"n\":
                        break
                    else:
                        print(\"Invalid choice. Please try again.\\n\")



            else:
                print(\"Invalid input. Please try again.\\n\")

    def mi():

        global user
        global pw
        global name

        while True:

            userlogin = input(\"\\nEnter your login info to continue (Don't enter anything if you haven't set your login info yet):\\nUsername (Enter \\\'back\\\' to return to the settings menu): \")
            pwlogin = input(\"Password: \")

            if userlogin == src.username and pwlogin == src.password:

                print(\"Login successful.\")

                name = input(\"\\nWhat is your name? \")
                user = input(\"What is your new username? \")
                pw = input(\"What is your new password? \")

                print(\"\\nInformation modified successfully.\\n\")

                break

            elif userlogin == \"q\" or userlogin == \"quit\" or userlogin == \"exit\" or userlogin == \"close\" or userlogin == \"return\" or userlogin == \"back\":
                break

            else:
                print(\"Invalid login info. Please try again.\\n\")

    def appsettings():

        global hcl

        applist = [
            \"Checklist (cl)\"
        ]

        while True:

            app = input(\"\\nWhich app do you want to change settings for (type \\\'list\\\' to list modifiable apps or \\\'back\\\' to go back)? \").lower()

            if app == \"q\" or app == \"quit\" or app == \"close\" or app == \"exit\" or app == \"back\" or app == \"return\":
                break

            elif app == \"list\" or app == \"lst\" or app == \"l\":
                print()
                for i in applist:
                    print(\" -\", i)

            elif app == \"checklist\" or app == \"cl\":

                while True:

                    home = input(\"Do you want your checklist to be shown on your homepage? \").lower()

                    if home == \"yes\" or home == \"y\" or home == \"yea\" or home == \"ye\" or home == \"ya\" or home == \"yeah\" or home == \"yeh\" or home == \"yah\":
                        hcl = True
                        break
                    elif home == \"no\" or home == \"n\" or home == \"nay\" or home == \"nah\" or home == \"na\":
                        hcl = False
                        break
                    else:
                        print(\"Invalid choice. Please try again.\\n\")

            else:
                print(\"Invalid selection. Please try again.\\n\")


    settings = [
        \"Date and Time (dt)\",
        \"My Info (mi)\",
        \"App Settings (as)\"
    ]

    while True:

        choice = input(\"\\nWhat setting do you want to change (type \\\'settings\\\' for a list of settings you can change or \\\'quit\\\' to close the app)? \").lower()

        if choice == \"return\" or choice == \"r\" or choice == \"back\" or choice == \"b\" or choice == \"exit\" or choice == \"close\" or choice == \"q\" or choice == \"quit\":
            print(\"\\nApp Closed.\")
            break

        elif choice == \"settings\" or choice == \"sects\" or choice == \"sections\" or choice == \"st\":
            print()
            for i in settings:
                print(\" - \"+i)

        elif choice == \"dt\" or choice == \"date and time\" or choice == \"dateandtime\" or choice == \"d&t\" or choice == \"date & time\":
            dt()

        elif choice == \"mi\" or choice == \"my info\" or choice == \"myinfo\" or choice == \"info\":
            mi()

        elif choice == \"app settings\" or choice == \"appsettings\" or choice == \"as\":
            appsettings()

        else:
            print(\"Invalid input. Please try again.\\n\")

    write = f\\\"\\\"\\\"
from datetime import datetime as dt

dtf = \\\"{dtf}\\\"
tf = \\\"{tf}\\\"
d = dt.now().strftime(dtf)
t = dt.now().strftime(tf)
username = \\\"{user}\\\"
password = \\\"{pw}\\\"
name = \\\"{name}\\\"
hcl = {hcl}
    \"\"\"

    source = open("settingsource.py", "w")
    source.write(write)
"""
    taf = """
def taf():

    while True:

        import numpy as np

        method = input(\"Enter the method you want to use here (\\\'quit\\\' to quit, \\\'bxh\\\' for base and height or \\\'hf\\\' to use Heron's formula): \")

        if method == \"q\" or method == \"quit\" or method == \"exit\" or method == \"close\":
            print(\"\\nApp Closed.\")
            break

        elif method == \"bxh\":

            b = float(input(\"\\nEnter the base here: \"))
            h = float(input(\"Enter the height here: \"))
            unit = input(\"Enter the unit in here: \")

            area = b * h / 2

            print(\"The area of this triangle is\", str(area)+unit, \"squared.\")

        elif method == \"hf\":

            a = float(input(\"Enter the first side length in here: \"))
            b = float(input(\"Enter the second side length in here: \"))
            c = float(input(\"Enter the third side length in here: \"))
            unit = input(\"Enter the unit in here: \")
            s = (a+b+c)/2
            asqr = s*(s-a)*(s-b)*(s-c)
            area = np.sqrt(asqr)

            print(\"The area of this triangle is\", str(area)+unit, \"squared.\")

        else:
            print(\"Invalid input. Please try again.\")
"""

    acts = [
        " - List possible actions: \'actions\'",
        " - List available apps: \'apps\'",
        " - Install an app: \'install\'",
        " - Delete an app: \'delete\'",
        " - Close the app store: \'quit\'"
    ]
    apps = [
        " - Binomial Distribution Calculator (bdc)",
        " - Calculator (calc)",
        " - Central Angle Calculator (cac)",
        " - Charts (ct)",
        " - Checklist (cl)",
        " - Charts Texture Dictionary (ctd)",
        " - DataFrames (df)",
        " - File Manager (fm)",
        " - Guess The Number (gtn)",
        " - Morse Code Converter (mcc)",
        " - Random Number Generator (rng)",
        " - Random Password Generator (rpg)",
        " - Rock Paper Scissors (rps)",
        " - Settings",
        " - Triangle Area Finder (taf)",
        " - Install all apps (all)"
    ]


    def install():

        while True:

            app = input("What app do you want to install (type \'back\' to go back)? ").lower()

            if app == "home" or app == "back" or app == "return" or app == "q" or app == "quit" or app == "close" or app == "exit":
                break

            else:

                if app == "binomial distribution calculator" or app == "bdc" or app == "binomial_distribution_calculator":
                    print(f"The {app} app was installed successfully.")
                    app = open("Binomial_Distribution_Calculator.py", "w")
                    app.write(bdc)

                elif app == "calculator" or app == "calc":
                    print(f"The {app} app was installed successfully.")
                    app = open("Calculator.py", "w")
                    app.write(calc)

                elif app == "central angle calculator" or app == "cac" or app == "central_angle_calculator":
                    print(f"The {app} app was installed successfully.")
                    app = open("Central_Angle_Calculator.py", "w")
                    app.write(cac)

                elif app == "charts" or app == "charts" or app == "ct":
                    print(f"The {app} app was installed successfully.")
                    app = open("Charts.py", "w")
                    app.write(ct)

                elif app == "checklist" or app == "cl":
                    print(f"The {app} app was installed successfully.")
                    app = open("Checklist.py", "w")
                    app.write(cl)

                elif app == "ctd" or app == "chart texture dictionary" or app == "charttexturedictionary":
                    print(f"The {app} app was installed successfully.")
                    app = open("ChartTextureDictionary.py", "w")
                    app.write(ctd)

                elif app == "df" or app == "dataframes" or app == "dataframe" or app == "dfs":
                    print(f"The {app} app was installed successfully.")
                    app = open("DataFrames.py", "w")
                    app.write(dfs)

                elif app == "file_manager" or app == "fm" or app == "file manager":
                    print(f"The {app} app was installed successfully.")
                    app = open("File_Manager.py", "w")
                    app.write(fm)

                elif app == "gtn" or app == "guess the number" or app == "guess_the_number":
                    print(f"The {app} app was installed successfully.")
                    app = open("Guess_The_Number.py", "w")
                    app.write(gtn)

                elif app == "morse code converter" or app == "morsecodeconverter" or app == "morse_code_converter" or app == "mcc":
                    print(f"The {app} app was installed successfully.")
                    app = open("Morse_Code_Converter.py", "w")
                    app.write(mcc)

                elif app == "rng" or app == "randomnumbergenerator" or app == "random number generator":
                    print(f"The {app} app was installed successfully.")
                    app = open("RandomNumberGenerator.py", "w")
                    app.write(rng)

                elif app == "random password generator" or app == "rpg" or app == "randompasswordgenerator":
                    print(f"The {app} app was installed successfully.")
                    app = open("RandomPasswordGenerator.py", "w")
                    app.write(rpg)

                elif app == "rock paper scissors" or app == "rock_paper_scissors" or app == "rps":
                    print(f"The {app} app was installed successfully.")
                    app = open("Rock_Paper_Scissors.py", "w")
                    app.write(rps)

                elif app == "settings":
                    print(f"The {app} app was installed successfully.")
                    app = open("Settings.py", "w")
                    app.write(settings)

                elif app == "triangleareafinder" or app == "triangle area finder" or app == "taf":
                    print(f"The {app} app was installed successfully.")
                    app = open("TriangleAreaFinder.py", "w")
                    app.write(taf)

                elif app == "everything" or app == "all" or app == "install everything" or app == "install all apps" or app == "inst all" or app == "inst everything" or app == "inst all apps":
                    print("\nInstalling all apps...\n")
                    app = open("Binomial_Distribution_Calculator.py")
                    app.write(bdc)
                    app = open("Calculator.py")
                    app.write(calc)
                    app = open("Charts.py")
                    app.write(ct)
                    app = open("ChartTextureDictionary.py")
                    app.write(ctd)
                    app = open("Checklist.py")
                    app.write(cl)
                    app = open("DataFrames.py")
                    app.write(dfs)
                    app = open("File_Manager.py")
                    app.write(fm)
                    app = open("Guess_The_Number.py")
                    app.write(gtn)
                    app = open("Morse_Code_Converter.py")
                    app.write(mcc)
                    app = open("RandomNumberGenerator.py")
                    app.write(rng)
                    app = open("RandomPasswordGenerator.py")
                    app.write(rpg)
                    app = open("Rock_Paper_Scissors.py")
                    app.write(rps)
                    app = open("Settings.py")
                    app.write(settings)
                    app = open("TriangleAreaFinder.py")
                    app.write(taf)
                    print("All apps installed successfully.\n")

                else:
                    print(f"{app} is not an app on the AarOS console.")

    def delete():

        while True:

            app = input("What app do you want to delete (type \'back\' to go back)? ").lower()

            if app == "home" or app == "back" or app == "return" or app == "q" or app == "quit" or app == "close" or app == "exit":
                break

            else:

                if app == "binomial distribution calculator" or app == "bdc" or app == "binomial_distribution_calculator":
                    os.remove("Binomial_Distribution_Calculator.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "calculator" or app == "calc":
                    os.remove("Calculator.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "central angle calculator" or app == "cac" or app == "central_angle_calculator":
                    os.remove("Central_Angle_Calculator.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "charts" or app == "charts" or app == "ct":
                    os.remove("Charts.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "checklist" or app == "cl":
                    os.remove("Checklist.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "ctd" or app == "chart texture dictionary" or app == "charttexturedictionary":
                    os.remove("ChartTextureDictionary.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "df" or app == "dataframes" or app == "dataframe" or app == "dfs":
                    os.remove("DataFrames.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "file_creator_and_editor" or app == "fce" or app == "file creator and editor":
                    os.remove("File_Creator_and_Editor.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "gtn" or app == "guess the number" or app == "guess_the_number":
                    os.remove("Guess_The_Number.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "morse code converter" or app == "morsecodeconverter" or app == "morse_code_converter" or app == "mcc":
                    os.remove("Morse_Code_Converter.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "rng" or app == "randomnumbergenerator" or app == "random number generator":
                    os.remove("RandomNumberGenerator.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "random password generator" or app == "rpg" or app == "randompasswordgenerator":
                    os.remove("RandomPasswordGenerator.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "rock paper scissors" or app == "rock_paper_scissors" or app == "rps":
                    os.remove("Rock_Paper_Scissors.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "settings":
                    os.remove("Settings.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "triangleareafinder" or app == "triangle area finder" or app == "taf":
                    os.remove("TriangleAreaFinder.py")
                    print(f"The {app} app was removed successfully.")

                elif app == "everything" or app == "all":
                    print("\nDeleting all apps...\n")
                    os.remove("Binomial_Distribution_Calculator.py")
                    os.remove("Calculator.py")
                    os.remove("Charts.py")
                    os.remove("ChartTextureDictionary.py")
                    os.remove("Checklist.py")
                    os.remove("DataFrames.py")
                    os.remove("File_Manager.py")
                    os.remove("Guess_The_Number.py")
                    os.remove("Morse_Code_Converter.py")
                    os.remove("RandomNumberGenerator.py")
                    os.remove("RandomPasswordGenerator.py")
                    os.remove("Rock_Paper_Scissors.py")
                    os.remove("Settings.py")
                    os.remove("TriangleAreaFinder.py")
                    print("All apps deleted successfully.\n")


                else:
                    print(f"{app} is not an app on the AarOS console.")

    while True:

        choice = input("\nWhat do you want to do (type \'actions\' for a list of things that you can do)? ").lower()

        if choice == "q" or choice == "quit" or choice == "close" or choice == "exit":
            print("\nApp Closed.")
            break

        elif choice == "acts" or choice == "actions" or choice == "choices":
            print()
            for i in acts:
                print(i)

        elif choice == "apps" or choice == "list" or choice == "lst" or choice == "l" or choice == "applications" or choice == "list apps" or choice == "list applications" or choice == "lst apps" or choice == "lst applications" or choice == "l apps" or choice == "l applications":
            print()
            for i in apps:
                print(i)

        elif choice == "del" or choice == "delete" or choice == "remove" or choice == "uninstall" or choice == "uninst":
            delete()

        elif choice == "install" or choice == "inst" or choice == "download" or choice == "get":
            install()

        else:
            print("Invalid choice. Please try again.")
