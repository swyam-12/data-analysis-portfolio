import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'OrderDate': ['2024-01-01', '2024-01-05', '2024-02-10', '2024-02-15', '2024-03-01'],
    'Sales': [200, 300, 400, 250, 500],
    'Product': ['A', 'B', 'A', 'C', 'B']
}

df = pd.read_csv("sales_data.csv")

# Convert date
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# 1. Monthly Sales Analysis
monthly_sales = df.resample('M', on='OrderDate')['Sales'].sum()

# 2. Product Performance
product_sales = df.groupby('Product')['Sales'].sum()

# 📈 Graph 1: Monthly Sales Trend
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show()

# 📊 Graph 2: Product Sales
product_sales.plot(kind='bar')
plt.title("Product Performance")
plt.show()

# 🧠 Insights (print)
print("\n--- BUSINESS INSIGHTS ---")
print("Total Sales:", df['Sales'].sum())
print("Best Product:", product_sales.idxmax())
print("Average Sales:", df['Sales'].mean())