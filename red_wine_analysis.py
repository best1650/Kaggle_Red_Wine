import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',100)
red_wine_df = pd.read_csv("winequality-red.csv")


def main():
    # Red Wine Column Name list
    print(red_wine_df.columns)
    # First 10 lines of the data
    print(red_wine_df.head())
    # Information about the data columns
    red_wine_df.info()

    # Width = 10, Height = 6
    fig = plt.figure(figsize = (10,6))
    sns.barplot(x = "quality", y = "fixed acidity", data = red_wine_df)
    #plt.show()



if __name__ == "__main__":
    main()
