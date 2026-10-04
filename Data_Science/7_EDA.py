#EDA = understanding the data before doing deeper analysis or machine learning.
#Data Cleaning
#Data Transormation
#Agregation and filtering

#Identifing Paterns, trends, Colleration

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#laoad tatanic data
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#inspect data 
print(df.info())
print(df.describe()) 

#handle the missing values 
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# remove duplicates
df = df.drop_duplicates()

#inspect data 
print(df.info())
print(df.describe()) 

#filter data Pasiger in first class
first_class = df[df["Pclass"] == 1]
print("First Class Passengers : \n", first_class.head())

# bar chart: survival rate by class 
survival_by_class= df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate by class")
plt.ylabel("Survilal Rate")
plt.show()

#  histogram age distribution
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distrbution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha= 0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

#bar chart: survival rate by sex
survival_by_sex = df.groupby("Sex")["Survived"].count()
print(survival_by_sex)

#Identify and Iterpret Patterns and Anomalies

##DataSet EDA Report
# Dataset contains 891 rows and 12 columns.
# Missing values handled for Age (filled with median) and Embarked (filled with mode).
# 2. Key Insights
# Survival rates are highest for first-class passengers (62%) and lowest for third-class customers (24%).
# The majority of passengers are aged between 20–40 years.
# A positive correlation exists between fare and survival.
# 3. Visual Insights
# Screenshots
