def ctd():

    print("\n" + "-" * len("Chart Texture Dictionary") + "\nChart Texture Dictionary\n" + "-" * len("Chart Texture Dictionary"))

    line = [
        ": | A simple dot texture.",
        "-- | A simple dotted line texture.",
        "- | A simple regular line texture",
        "-. | A dash-dot line pattern.",
        "-o | An enlarged point texture."
    ]

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
        ["seaborn-muted", "A brightened version of the original seaborn texture."],
        ["seaborn-pastel", "An extremely brightened version of the original seaborn texture."],
        ["tableau-colorblind10", "A version of the default texture optimized for the colourblind."]
    ]

    while True:

        try:

            ctype = input("\nWhich texture type do you want to see (line graph textures - \'line\', style sheets - \'style\' or do you want to quit - \'quit\')? ").lower()

            if ctype == "quit" or ctype == "q" or ctype == "exit" or ctype == "close":
                print("\nApp Closed.")
                break

            elif ctype == "line" or ctype == "plot":
                 for i in line:
                     print(" -", i)

            elif ctype == "style" or ctype == "sheets" or ctype == "ss":
                for i in style:
                    print(" -", i[0]+":", i[1])

            else:
                print("Invalid input. Please try again.\n")

        except:
            print("There was an error. Please try again.")
