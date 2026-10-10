#drop missing vlues 

import pandas as pd
from pathlib import Path

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df3 = pd.read_csv(url)  # Load a CSV file from a URL into a DataFrame

print(df3.head(3))


df3["source"] = "IRIS Dataset"
print("Df with new column \n", df3.head(3))

#W Pandas parametr axis określa, co usuwasz: axis=0 — wiersze, axis=1 — kolumny
### Usunięcie kolumny
#df.dropna(axis=0)      # remove rows with missing values
#df.dropna(axis=1)      # remove columns with missing values
#df.dropna(subset=["age"])  # remove rows where age is missing

df4 = df3.drop(columns=["source"]) 

print("Df4 after dropping column 'source' \n", df4.head(10))

#### Uzupełnianie brakujących wartości:
# ffill (forward fill) kopiuje ostatnią znaną wartość w dół.
# bfill (backward fill) kopiuje następną znaną wartość w górę.
df_missing = pd.DataFrame({"source": ["IRIS Dataset", None, None, "Other Dataset", None]})

df_missing["source_ffill"] = df_missing["source"].ffill()
df_missing["source_bfill"] = df_missing["source"].bfill()

print("Filling missing values with ffill and bfill:\n", df_missing)
df_sales = pd.DataFrame({
    "sales": [50, None, 300]
})
print("Original sales DataFrame:\n", df_sales)
#ffill() kopiuje poprzednią wartość, bfill() kopiuje następną wartość, interpolate() oblicza wartość pomiędzy sąsiadującymi wartościami.
#df_sales["sales"] = df_sales["sales"].interpolate()


df_sales=df_sales.fillna(0)  # Fill missing values with 0


print("Filling missing values with interpolate:\n", df_sales)
#rename() zmienia nazwy kolumn w DataFrame. Możesz przekazać słownik, w którym klucze to stare nazwy kolumn, a wartości to nowe nazwy kolumn.
# df_sales= df_sales.rename(columns={"sales": "sales_promo"})
# print("Sales DataFrame with promo values:\n", df_sales)

#add new column with promo values
df_salespromo = df_sales.copy()  # Create a copy of the original DataFrame
df_salespromo["sales_promo"] = df_salespromo["sales"]*0.8 
print("Sales DataFrame with promo values:\n", df_salespromo)

#### Combining two DataFrames using concat() or merge(). The concat() function is used to concatenate two or more DataFrames along a particular axis (rows or columns). 
# The merge() function is used to combine two DataFrames based on a common column or index.
# join() is used to combine two DataFrames based on their index. It is similar to merge(), but it only works with the index of the DataFrames.
df_combined_cols = pd.concat([df_sales, df_salespromo], axis=1)  # Concatenate along columns
print("Combined DataFrame:\n", df_combined_cols)

df_combined_rows = pd.concat([df_sales, df_salespromo], axis=0)  # Concatenate along rows
print("Combined DataFrame (rows):\n", df_combined_rows)

marged_df = pd.merge(df_sales, df_salespromo, on="sales")
print("Merged DataFrame:\n", marged_df)

# join() combines DataFrames using their indexes.
df_products = pd.DataFrame(
    {"product": ["Notebook", "Pen", "Backpack"]},
    index=[101, 102, 103],
)
df_prices = pd.DataFrame(
    {"price": [12.50, 2.00, 45.00]},
    index=[101, 102, 103],
)


df_products_with_prices = df_products.join(df_prices)
print("Products joined with prices:\n", df_products_with_prices)

df_products = pd.DataFrame(
    {"product": ["Notebook", "Pen", "Backpack"]},
    index=[101, 102, 103],
)

df_prices = pd.DataFrame(
    {"price": [12.50, 2.00, 45.00]},
    index=[101, 102, 103],
)

df_products_with_prices = df_products.join(df_prices)
print(df_products_with_prices)