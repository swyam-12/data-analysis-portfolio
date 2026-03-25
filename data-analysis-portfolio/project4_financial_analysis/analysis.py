import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("finance_data.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# 1. Average Price per Stock
avg_price = df.groupby('Stock')['Price'].mean()

# 📊 Graph 1: Average Price
avg_price.plot(kind='bar')
plt.title("Average Stock Price")
plt.show()

# 📊 Graph 2: Price Trend for Stock A
stock_a = df[df['Stock'] == 'A']
plt.plot(stock_a['Date'], stock_a['Price'])
plt.title("Stock A Price Trend")
plt.show()

# 📊 Graph 3: All Stocks Trend
for stock in df['Stock'].unique():
    data = df[df['Stock'] == stock]
    plt.plot(data['Date'], data['Price'], label=stock)

plt.legend()
plt.title("Stock Price Trends")
plt.show()

# 🧠 Insights
print("\n--- FINANCIAL INSIGHTS ---")
print("Best Performing Stock:", avg_price.idxmax())