def df():

    print("-"*len("DataFrames")+"\nDataFrames\n"+"-"*len("DataFrames"))
    print("Note: If more than 5 columns are selected, DataFrame will be displayed in mass rows with 5 columns displayed per row.\n\nLoading...\n\n")

    import warnings
    import pandas as pd
    from sklearn.linear_model import LinearRegression as lreg
    from sklearn.model_selection import train_test_split as tts

    warnings.filterwarnings("ignore")
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    while True:

        sdf = input("Do you want to keep using the same DataFrame for this session? ").lower()

        if sdf == "yes" or sdf == "y" or sdf == "yea" or sdf == "ye" or sdf == "ya" or sdf == "yeah" or sdf == "yeh" or sdf == "yah":

            url = input("\nEnter the download link for the dataframe that you want to view (or type \'quit\' to quit): ")

            if url == "q" or url == "quit" or url == "close" or url == "exit" or url == "return":
                print("\nApp Closed.")
                break

            else:
                print("\nLoading DataFrame...\n")
                df = pd.read_csv(url)
                break

        elif sdf == "no" or sdf == "n" or sdf == "nay" or sdf == "nah" or sdf == "na":
            break

        else:
            print("Invalid response.\n")

    while True:

        if url == "q" or url == "quit" or url == "close" or url == "exit" or url == "return":
            break

        if sdf == "no" or sdf == "n" or sdf == "nay" or sdf == "nah" or sdf == "na":

            url = input("\nEnter the download link for the dataframe that you want to view (or type \'quit\' to quit): ")

            if url == "q" or url == "quit" or url == "close" or url == "exit" or url == "return":
                print("\nApp Closed.")
                break

            else:
                print("\nLoading DataFrame...\n")
                df = pd.read_csv(url)


        action = input("\nWhat do you want to do (type \'formats\' to view formats that you can use or \'quit\' to quit)? ").lower()

        fts = [
            "regular (reg): A regular table view of the DataFrame.",
            "information (info): Shows an overview of the contents in the DataFrame.",
            "describe (desc): Shows numerical statistics like mean, standard deviation, etc.",
            "value counts (vc): Shows the number of times each value appears in a column.",
            "prediction model (pred): Creates a prediction model that can predict values based on the data that is given.",
            "find value (fv): Shows occurrences of a chosen value and the location(s) of those occurrences.",
            "find and replace (fr): Shows occurrences of a chosen value and the location(s) of those occurrences, and allows you to replace them with another value."
        ]

        if action == "q" or action == "quit" or action == "close" or action == "exit" or action == "return":
            print("\nApp Closed.")
            break

        elif action == "formats" or action == "fts" or action == "f":
            print()
            for i in fts:
                print(" -", i)

        else:

            if action == "regular" or action == "reg" or action == "plain" or action == "df" or action == "dataframe" or action == "table":

                column = input("Enter the column you want to search for in here (type \'all\' to view all columns or \'multi\' to view multiple columns): ").lower()

                if column == "all":
                    s = int(input("Enter the starting row number for your selection: "))
                    e = int(input("Enter the ending row number for your selection: ")) + 1
                    print(f"\n{df[s:e]}")

                elif column == "multi" or column == "multiple":

                    cnum = int(input("How many columns do you want to select? "))
                    cols = []

                    for i in range(cnum):
                        col = input(f"Column {i + 1}: ")
                        if col in df.columns:
                            cols.append(col)
                        else:
                            print(f"The \'{col}\' column is not in this DataFrame.\n")
                            break

                    if len(cols) == cnum:
                        s = int(input("Enter the starting row number for your selection: "))
                        e = int(input("Enter the ending row number for your selection: ")) - 1

                        print(f"\n{df.loc[s:e, cols]}")

                    else:
                        pass

                else:

                    if column in df.columns:
                        s = int(input("Enter the starting row number for your selection: "))
                        e = int(input("Enter the ending row number for your selection: ")) - 1
                        print(f"\n{df.loc[s:e, column]}")
                    else:
                        print("Invalid column. Please try again.")

            elif action == "info" or action == "information":
                print(df.info())

            elif action == "desc" or action == "describe" or action == "description":
                print(df.describe())

            elif action == "value counts" or action == "vc" or action == "value_counts":
                column = input("Enter the column you want to search for in here: ").lower()
                if column in df.columns:
                    print(df[column].value_counts())
                else:
                    print("Invalid column. Please try again.")

            elif action == "pred" or action == "prediction" or action == "predict" or action == "predict value" or action == "p" or action == "prediction model":

                cnum = input("How many columns do you want to use as feature (x axis) variables (type \'auto\' to automatically select the best columns for prediction)? ").lower()
                s = input("Enter the starting row number for your selection (type \'all\' to select all rows - this is more accurate but will result in a large predicted output): ")

                if s == "all" or s == "everything":
                    s = 0
                    e = df.shape[0]

                else:
                    e = int(input("Enter the ending row number for your selection: ")) + 1

                if cnum == "auto" or cnum == "automatic":

                    predcol = input("What column do you want to predict? ")
                    t = df.loc[s:e, predcol]

                    print("\nCreating model...\n")

                    cols = []

                    for i in range(len(df.corr()[predcol])):
                        if df.corr()[predcol][i] >= 0.5:
                            cols.append(df.corr()[predcol].index[i])

                else:

                    cnum = int(cnum)
                    cols = [input(f"Column {i+1}: ") for i in range(cnum)]
                    t = df[input("What column do you want to predict? ")]

                    print("\nCreating model...\n")

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

                print(f"Mean of Predicted Values: {pred.mean()}\n\nModel Accuracy: {lr.score(xtest, ytest)*100}%.")

                view = input("Would you like to view a list of the predicted values? ").lower()

                if view == "yes" or view == "y" or view == "ye" or view == "ya" or view == "yep" or view == "yeah" or view == "yea" or view == "yah":
                    print("\nPredicted Values:\n")
                    for i in pred:
                        print(f" - {i}")

            elif action == "find" or action == "search" or action == "value search" or action == "find value" or action == "vs" or action == "fv":

                cnum = input("How many columns do you want to use (type \'all\' for all columns)? ")

                if cnum == "all":
                    cols = [i for i in df.columns]
                else:
                    cnum = int(cnum)
                    cols = []

                    for i in range(cnum):
                        col = input(f"Column {i + 1}: ")
                        if col in df.columns:
                            cols.append(col)
                        else:
                            print(f"The \'{col}\' column is not in this DataFrame.\n")
                            break


                value = input("What value do you want to search for? ").lower()
                view = input("Do you want to view the occurences of this value (y/n)? ").lower()

                for x in cols:

                    print(f"\n\'{x}\' Column:\n")
                    count = 0

                    for y in df[x]:
                        if str(y).lower() == value:
                            count += 1

                    print(f"Found {count} occurences of {value}.\n")

                    if view == "yes" or view == "y" or view == "ye" or view == "yeah" or view == "ya" or view == "yep" or view == "yea" or view == "yah" or view == "yeh":

                        print("Occurences:\n")

                        for z in range(len(df[x])):
                            if str(df[x][z]).lower() == value:
                                print(f" - Row {z+1}")

            elif action == "find and replace" or action == "fr" or action == "replace" or action == "rep":

                print("\nDisclaimer: DataFrame modifications will only be applied in the current session.\n")

                value = input("What value do you want to search for? ").lower()
                rep = input("What value do you want to replace it with? ")
                view = input("Do you want to view the occurences of this value (y/n)? ").lower()

                for x in df.columns:

                    print(f"\n\'{x}\' Column:\n")
                    count = 0
                    lst = []

                    for y in df[x]:
                        if str(y).lower() == value:
                            count += 1

                    if count == 0:
                        print(f"Could not find occurences of {value}.\n")

                    else:

                        if view == "yes" or view == "y" or view == "ye" or view == "yeah" or view == "ya" or view == "yep" or view == "yea" or view == "yah" or view == "yeh":

                            print("Occurences:\n")

                            for o in range(len(df[x])):
                                if str(df[x][y]).lower() == value:
                                    print(f" - Row {o+1}")

                        print(f"Found {count} occurences of {value}.\n")

                        replace = input(f"\nDo you want to replace the occurences of \'{value}\' in the \'{x}\' column (y/n)? ").lower()

                        if replace == "yes" or replace == "y" or replace == "ye" or replace == "yeah" or replace == "ya" or replace == "yep" or replace == "yea" or replace == "yah" or replace == "yeh":

                            for i in df[x]:

                                if str(df[x][y]).lower() == str(value).lower():
                                    lst.append(rep)

                                else:
                                    lst.append(str(df[x][y]).lower())

                            df.drop(columns=[x])
                            df[x] = pd.Series(lst)

            else:
                print("Invalid choice. Please try again.\n")
