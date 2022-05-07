def charts():

    print("\n" + "-" * 6 + "\nCharts\n" + "-" * 6 + "\n")
    print("(Disclaimer: You may have to wait a few seconds to a minute for the program to create your chart; once you create one, you will need to close it to resume the app)\n\nLoading...")

    import numpy as np
    import pandas as pd
    import seaborn as sn
    import matplotlib.pyplot as plt

    style = [
        ["default", "The default look for all your charts."],
        ["classic", " A vibrant, outlined chart texture."],
        ["Solarize_Light2", "A chart texture that gives elements a brighter, more yellowish look."],
        ["bmh", "A chart texture that gives elements a more greyish look, and adds a light grey grid in the background."],
        ["dark_background", "A simple dark background for all your charts."],
        ["fast", "Adds a bit more tone to the default texture."],
        ["fivethirtyeight", "Adds more tone to the default texture and thickens lines in line graphs."],
        ["ggplot", "Adds a reddish tint to the default texture."],
        ["seaborn", "Adds a greyish tint to the default chart texture."],
        ["seaborn-bright", "A brighter version of the seaborn chart texture."],
        ["seaborn-colourblind", "A version of the seaborn chart texture optimized for the colourblind."],
        ["seaborn-dark", "A combination of the seaborn chart texture and the default chart texture."],
        ["seaborn-dark-palette", "The seaborn-bright texture, but with darker colours."],
        ["seaborn-deep", "Adds a bit more tone to the original seaborn texture."],
        ["", ""]
    ]
    stylenames = [i[0] for i in style]


    def bp():

        url = input("Enter the full file download URL in here: ")
        section = input("What section do you want to use? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))

        sn.boxplot(data=file, x=file[section][s:e + 1])

    def hg():

        url = input("Enter the full file download URL in here: ")
        format = input("What format do you want to use (\'pyplot\' or \'seaborn\')? ")
        divs = int(input("How many divisions do you want in your histogram? "))
        section = input("What section do you want to use? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))

        if format == "pyplot" or format == "plt" or format == "matplotlib.pyplot":
            plt.hist(url[section][s:e + 1], bins=divs)

        elif format == "sn" or format == "sns" or format == "seaborn":
            sn.displot(file[section][s:e + 1], bins=divs, kde=True)

        else:
            print("Invalid input. Please try again.")

    def bar():

        url = input("Enter the full file download URL in here: ")
        section = input("What section do you want to use? ")
        palette = input("What colour palette would you like to use? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))
        addhue = input("Do you want to use category separation in your graph (y/n)? ")

        while True:

            if addhue.lower() == "y" or addhue.lower() == "yes":
                hue = input("What category do you want to use to separate the information? ")
                sn.countplot(x=section[s:e + 1], data=file, palette=palette, hue=hue)

            else:
                sn.countplot(x=section[s:e + 1], data=file, palette=palette)

    def line():

        url = input("Enter the full file download URL in here: ")
        section = input("What section do you want to use? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))
        y = np.arange(len(file[section][s:e]))
        format = input("What format do you want to use (pyplot - \'plt\' or seaborn \'sn\')? ")

        while True:

            if format == "pyplot" or format == "plt":

                cxt = input(
                    "What colour and texture do you want to use - enter the starting letter of the colour followed by a texture (check Chart Texture Dictionary for textures)?")
                print("(The section", section, "is on the x axis)")
                plt.plot(file[section][s:e], y, cxt)
                break

            elif format == "seaborn" or format == "sns" or format == "sn":

                palette = input("What colour palette would you like to use? ")
                addhue = input("Do you want to use category separation in your graph (y/n)? ")

                while True:

                    if addhue.lower() == "y" or addhue.lower() == "yes":
                        hue = input("What category do you want to use to separate the information? ")
                        print("\n(The section", "\'" + section + "\'", "is on the x axis)")
                        sn.lineplot(data=file[s:e], x=section, y=y, palette=palette, hue=hue)
                        break

                    else:
                        print("\n(The section", "\'" + section + "\'", "is on the x axis)")
                        sn.lineplot(data=file[s:e], x=section, y=y, palette=palette)
                        break

                break

    def scatter():

        url = input("Enter the full file download URL in here: ")
        section = input("What section do you want to use? ")
        palette = input("What colour palette would you like to use? ")
        mkr = input("What marker would you like to use? ")
        size = int(input("What marker size (pixels) do you want to use? "))

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))
        y = np.arange(len(file[section][s:e]))
        addhue = input("Do you want to use category separation in your graph (y/n)? ")

        while True:

            if addhue.lower() == "y" or addhue.lower() == "yes":
                hue = input("What category do you want to use to separate the information? ")
                print("\n(The section", "\'" + section + "\'", "is on the x axis)")
                sn.scatterplot(data=file[s:e], x=section, y=y, palette=palette, marker=mkr, size=size, hue=hue)
                break

            else:
                print("\n(The section", "\'" + section + "\'", "is on the x axis)")
                sn.scatterplot(data=file[s:e], x=section, y=y, palette=palette, marker=mkr, size=size)
                break

    def regplot():

        url = input("Enter the full file download URL in here: ")
        section = input("What section do you want to use? ")
        color = input("What colour would you like to use? ")
        mkr = input("What marker would you like to use? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))
        y = np.arange(len(file[section][s:e]))

        print("\n(The section", "\'" + section + "\'", "is on the x axis)")
        sn.regplot(x=file[section][s:e], y=y, color=color, marker=mkr)

    def pplt():

        url = input("Enter the full file download URL in here: ")
        palette = input("What colour palette would you like to use? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))

        sn.pairplot(file[s:e], palette=palette)

    def pie():

        url = input("Enter the full file download URL in here: ")
        section = input("What section do you want to use? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)

        while True:

            if section in file.columns:
                break
            else:
                print("Invalid section choice.")
                return 0

        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: ")) + 1
        sectnum = file[section].value_counts().shape[0]

        expl = []
        colours = []

        addexpl = input("Do you want to separate your pie chart sections from the center (y/n)? ")

        if addexpl.lower() == "yes" or addexpl.lower() == "y":

            for i in range(int(sectnum)):
                expl.append(
                    float(input(str(file[section].value_counts().index[i]) + " category separation perentage: ")) / 100)

        else:
            expl = None

        addcolour = input("Do you want to customize your pie chart section colours (y/n)? ")

        if addcolour.lower() == "yes" or addcolour.lower() == "y":

            for x in range(int(sectnum)):
                y = x + 1
                i = input("Colour " + str(y) + " (" + str(file[section].value_counts().index[x]) + ")" + ": ").lower()
                colours.append(i)

        else:
            colours = None

        tc = input("What text colour do you want to use? ").lower()

        plt.pie(file[section][s:e].value_counts(), autopct="%1.2f%%", labels=file[section][s:e].value_counts().index, shadow=True, colors=colours, explode=expl, textprops={"color": tc})

    def hm():

        url = input("Enter the full file download URL in here: ")
        colour = input("What colour would you like to use (enter in a valid heatmap colour format)? ")

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))

        print("Columns are represented in order - top to bottom and left to right.")
        sn.heatmap(file[s:e].corr(), cmap=colour, annot=True)

    def jp():

        url = input("Enter the full file download URL in here: ")
        section = input("What section do you want to use? ")
        palette = input("What colour palette would you like to use? ")
        size = int(input("What graph side length (pixels) do you want to use? "))

        print("\nImporting file...\n")

        file = pd.read_csv(url)
        s = int(input("Enter the starting selection row number here: "))
        e = int(input("Enter the ending selection row number here: "))
        y = np.arange(len(file[section][s:e]))

        if section in file.columns:
            print()
        else:
            print("Invalid section.")

        print("\n(The section", "\'" + section + "\'", "is on the x axis)")
        sn.jointplot(data=file[s:e], x=section, y=y, palette=palette, height=size)

    cts = [
        "boxplot: \'bp\'",
        "histogram: \'hg\'",
        "bar graph: \'bar\'",
        "line graph: \'line\'",
        "scatter graph: \'scatter\'",
        "full-scale scatter graph (for the entire DataFrame): \'fss\'",
        "regression plot: \'regplot\'",
        "joint bar and scatter plot: \'jp\'",
        "pie chart: \'pie\'",
        "heatmap: \'hm\'"
    ]

    while True:

        ctype = input("\nWhat type of chart would you like to use (type \'ctypes\' to view chart types or \'quit\' to quit)? ").lower()

        if ctype == "quit" or ctype == "q" or ctype == "exit" or ctype == "close":
            print("\nApp Closed.")
            break

        elif ctype == "ctypes" or ctype == "cts" or ctype == "chart types":

            print()

            for i in cts:
                print(" -", i)

            print()

        else:

            title = input("What title would you like to use for your chart? ")
            bg = input("What chart style do you want to use (view Chart Texture Dictionary for chart styles)? ")

            if bg not in stylenames:
                print("Invalid chart style. Please try again.")

            else:

                plt.style.use(bg)

                if ctype == "bp" or ctype == "boxplot":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    bp()
                    plt.show()

                elif ctype == "hg" or ctype == "histogram":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    hg()
                    plt.show()

                elif ctype == "bar" or ctype == "bar graph":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    bar()
                    plt.show()

                elif ctype == "line" or ctype == "line graph":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    line()
                    plt.show()

                elif ctype == "scatter" or ctype == "scatter plot":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    scatter()
                    plt.show()

                elif ctype == "regplot" or ctype == "regression plot" or ctype == "rplt":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    regplot()
                    plt.show()

                elif ctype == "jp" or ctype == "jointplot" or ctype == "joint plot" or ctype == "jplt":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    jp()
                    plt.show()

                elif ctype == "fss" or ctype == "pplt" or ctype == "full-scale scatter graph" or ctype == "pairplot":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    pplt()
                    plt.show()

                elif ctype == "pie" or ctype == "pie chart":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    pie()
                    plt.show()

                elif ctype == "hm" or ctype == "htmp" or ctype == "heatmap" or ctype == "heat map":
                    plt.figure(figsize=(20, 7))
                    plt.title(title)
                    hm()
                    plt.show()

                elif ctype == "jp" or ctype == "joint plot" or ctype == "jointplot":
                    plt.title(title)
                    jp()
                    plt.show()

                else:
                    print("Invalid chart type. Please try again.")


# charts()
# Test File: "https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/meteorite-landings/meteorite-landings.csv"
