import pandas as pd
from pathlib import Path

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df2 = pd.read_csv(url)  # Load a CSV file from a URL into a DataFrame

#Explore the structure of the DataFrame
# print("First 5 rows of the DataFrame: \n",df2.head(5))
# print("Last 5 rows of the DataFrame: \n",df2.tail(5))
# print(df2.info())  # Print a concise summary of the DataFrame

# print("Summary statistics of the DataFrame: \n", df2.describe())

selected_columns = df2[["species", "sepal_length"]] 
print("selected _columns:\ n", selected_columns)

filter_rows = df2[(df2["sepal_length"] > 5.0) & (df2["species"] == "setosa")]
print("Filtered rows:\n", filter_rows)

df2["source"] = "IRIS Dataset"

print("Df with new column \n", df2.head(10))