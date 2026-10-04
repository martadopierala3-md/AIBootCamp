#clean data by handling missing values, renaming columns, and combining DataFrames
# fill with mean, median, mode, ffill, bfill, interpolate, dropna, fillna

import pandas as pd
import numpy as np 

#create a DataFrame with missing values
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35 ],
    "Score": [85, 90, np.nan, 88]
} 

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df["Age"] = df["Age"].fillna(df["Age"].mean())  # Fill missing values in Age with the mean
df["Score"] = df["Score"].interpolate()  # Interpolate missing values in Score

print("modified DataFrame:\n", df)

#rename columns
df = df.rename(columns={"Name": "Student_Name", "Score":"Exam:Score"})

print("Rename columns \n", df)