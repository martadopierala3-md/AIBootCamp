import pandas as pd
from pathlib import Path

# # Pandas is a popular Python library for working with structured data. It provides:
# # DataFrame: table-like data structure with rows and columns
# # Series: one-dimensional labeled data
# s =pd.Series([10,20,30], index=['a','b','c']) # Create a Series with custom index
# print(s) # Display the Series

# data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]} # Create a dictionary of data
# print(data) # Display the dictionary
# df = pd.DataFrame(data) # Create a DataFrame from the dictionary
# print(df) # Display the DataFrame

# # Tools for filtering, cleaning, grouping, merging, and analyzing data
# # Support for reading files such as CSV, Excel, and SQL data

csv_path = Path(__file__).with_name("data.csv")
df = pd.read_csv(csv_path)  # Read a CSV file into a DataFrame
print(df)

df.to_csv("output.csv", index=False)
output_path = Path("output.csv")
print(f"Saved to {output_path}")

#ndex=False prevents pandas from adding an extra index column to the CSV.

print(df.head())  # Display the first few rows of the DataFrame
print(df.describe())  # Display summary statistics of the DataFrame

print(df.tail(3))  # Display the last 3 rows of the DataFrame
print(df.info())

print([df["Name"], df["Age"]])  # Access specific columns by name
# print(df['Age'])   # Access another specific column by name
#selecting rows based on a condition
print(df[df["Age"] > 25])  # Filter rows based on a condition   

#SELECTING by label
#df.iloc iloc selects rows and columns by numeric position.
print("First\n", df.iloc[0])        # First row
print("First 3 rows\n", df.iloc[0:3])      # First 3 rows
print("First column\n", df.iloc[:, 0])     # First column
print("First 2 columns\n", df.iloc[:, 0:2])   # First 2 columns
print("Value at first row, second column\n", df.iloc[0, 1])     # Value at first row, second column

