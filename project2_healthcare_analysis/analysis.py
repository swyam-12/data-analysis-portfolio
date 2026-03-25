import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("healthcare_data.csv")

# 1. Average Treatment Cost
avg_cost = df['TreatmentCost'].mean()

# 2. Outcome Count
outcome_count = df['Outcome'].value_counts()

# 3. Age Distribution
age_group = df['Age']

# 📊 Graph 1: Outcome Distribution
outcome_count.plot(kind='bar')
plt.title("Treatment Outcome Distribution")
plt.show()

# 📊 Graph 2: Treatment Cost by Gender
df.groupby('Gender')['TreatmentCost'].mean().plot(kind='bar')
plt.title("Avg Treatment Cost by Gender")
plt.show()

# 📊 Graph 3: Age Distribution
plt.hist(age_group)
plt.title("Age Distribution")
plt.show()

# 🧠 Insights
print("\n--- HEALTHCARE INSIGHTS ---")
print("Average Treatment Cost:", avg_cost)
print("Most Common Outcome:", outcome_count.idxmax())