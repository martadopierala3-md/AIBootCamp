import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
#df = pd.read_csv("C:\Users\marta\Documents\Marta\AIBootCamp\week2\plants.csv")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)  # Load a CSV file from a URL into a DataFrame

del df['species']
#print(df.head(10))
#can compute correlations between columns.
#Correlation shows association, not cause It only measures linear relationships
#A strong correlation does not necessarily mean one variable causes the other
correlation_matrix = df.corr()

print(correlation_matrix)

#plot  heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Coleration Heatmap")
plt.show()

 