import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

# 1. Create a revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# 2. Group by Country and sum the revenue
revenue_by_country = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

# 3. Print exact data values for the plot
print("Revenue by Country Data:", revenue_by_country.to_dict())

# 4. Plot a bar chart of total revenue by country
plt.figure(figsize=(12, 6))
sns.barplot(x=revenue_by_country.index, y=revenue_by_country.values, palette="viridis")
plt.xticks(rotation=90)
plt.ylabel("Total Revenue (GBP)")
plt.title("Total Revenue by Country")
plt.tight_layout()
plt.show()