import matplotlib.pyplot as plt

#line plot 
years= [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]
plt.plot(years, sales, label ="SalesTrend", color = "blue", marker= "o")
plt.title("Sales over years")
plt.xlabel("years")
plt.ylabel("sales")
plt.legend()
plt.show()

#bar chart
categories= ["Electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150 ]
plt.bar(categories, revenue, color="green")
plt.title("Revenue by Category")
plt.show()

#scatter plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]
plt.scatter(hours_studied, exam_scores, color ="red")
plt.title("Study hours vs exam scores")
plt.xlabel("hours studied")
plt.ylabel("exams scores")
plt.show()
