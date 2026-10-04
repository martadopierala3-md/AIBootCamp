# Group data by categorial column

import pandas as pd

data = {
    "Class" :["A", "B" , "A", "B" , "C", "C"],
    "Score" :[80, 90, 88, 72, 96, 80],
    "Age" : [15, 16, 15, 17, 16, 15]
}

df = pd.DataFrame(data)
print("orginal dataset\n", df)

grouped = df.groupby("Class").mean()

print(grouped)