#& uv pip install --python .\.venv\Scripts\python.exe matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
#basic plot
# x= [1,2,3,4]
# y =  [10,20,25,30]
# plt.plot(x, y)
# plt.show()

#line plot 
# plt.plot([1,2,3], [10,20,30], label="Trend")
# plt.title("Line Plot")
# plt.xlabel("x-Axis")
# plt.ylabel("y-Axis")
# plt.legend()
# plt.show()

#bar chart - categorical data comparision
# categories = ["elecronics","Clothing", "Gloceries"]
# revenue = [200, 400, 150]
# plt.bar(categories, revenue, color='green')
# plt.title("Revenue by Category")
# plt.show()

#A histogram shows how numerical values are distributed across ranges, called bins. For example, it can show how many values fall into ranges such as: 0–10, 10–20, 20–30
# data =[1 ,2 ,2 ,3 ,3 ,3, 4, 4, 4, 4]
# plt.hist(data, bins=4, color="green", edgecolor = "black")
# plt.title("Histogram")
# plt.show()

#A scatter plot is used to show the relationship between two numerical variables: one on the x-axis and one on the y-axis.

# x = [1, 2, 3, 4, 5]
# y = [10, 12, 25, 30, 45]
# plt.scatter(x, y, color = "red")
# plt.title("Scatter Plot")
# plt.xlabel("X axis Label")
# plt.ylabel("Y axis Label")
# plt.legend(["Data Set 1"])
# plt.show()

###Seaborn: automatic styling good default colors works well with pandas, easy to create statistical plots Very short summary:
#scatter plot in Seaborn = sns.scatterplot()
#histograms = sns.histplot()
#boxplots = sns.boxplot()
#display the numerical value inside each cell of a heatmap instead of just colors, you also see the actual numbers
#annot=False → only colors, no text annot=True → text labels inside each cell
data = np.random.rand(5,5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("HeatMap")
plt.show()