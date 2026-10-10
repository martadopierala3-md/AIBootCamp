

#group by operations in pandas
#In pandas, groupby lets you split a DataFrame by one or more columns and then apply an aggregation or transformation to each group.

import pandas as pd

df = pd.DataFrame({
    "region": ["North", "South", "North", "South"],
    "product": ["A", "A", "B", "B"],
    "sales": [10, 20, 30, 40]
})

# Group by region and sum sales
print("Sum by region \n", df.groupby("region")["sales"].sum())

print("Mean \n",df.groupby("region")["sales"].mean())
#multi agregation
df1 =  df.groupby("region").agg(
    total_sales=("sales", "sum"),
    avg_sales=("sales", "mean"),
)

print("agg \n",df1)

df2 = df.groupby("product").agg({
    "sales": ["sum", "mean", "max", "min"],
    "region": "count"
})

print("multi agg sum mean max min \n",df2)

#groupby = “group rows by a key and summarize them”
#pivot_table = “reshape that grouped summary into a table with rows/columns”

# sales by region and product
df3 = df.groupby(["region", "product"])["sales"].sum()
print("agg df3 \n",df3)

df4 = df.pivot_table(
    index="region",
    columns="product",
    values="sales",
    aggfunc="sum",
    fill_value=0
)

print("agg_pivot \n",df4)

#groupin with custom functions spread# custom: range within each group
df5 = df.groupby("region")["sales"].agg(lambda x: x.max() - x.min())
print("agg df5 min_max spread \n",df5)

def reange_func(x):
    return x.max() - x.min()

df6 = df.groupby("region")["sales"].agg(reange_func)

print("agg df6 min_max spread custom func \n",df6)