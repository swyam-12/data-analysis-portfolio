import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_data.csv")

# Total revenue
df['Revenue'] = df['Price'] * df['Quantity']

# 1. Revenue by Product
product_revenue = df.groupby('Product')['Revenue'].sum()

# 2. Revenue by Customer
customer_revenue = df.groupby('CustomerID')['Revenue'].sum()

# 📊 Graph 1: Product Revenue
product_revenue.plot(kind='bar')
plt.title("Revenue by Product")
plt.show()

# 📊 Graph 2: Customer Revenue
customer_revenue.plot(kind='bar')
plt.title("Revenue by Customer")
plt.show()

# 📊 Graph 3: Quantity Distribution
plt.hist(df['Quantity'])
plt.title("Quantity Distribution")
plt.show()

# 🧠 Insights
print("\n--- E-COMMERCE INSIGHTS ---")
print("Best Product:", product_revenue.idxmax())
print("Top Customer:", customer_revenue.idxmax())
print("Total Revenue:", df['Revenue'].sum())