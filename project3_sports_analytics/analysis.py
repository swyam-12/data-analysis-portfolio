import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sports_data.csv")

# 1. Total Goals by Player
player_goals = df.groupby('Player')['Goals'].sum()

# 2. Team Performance
team_goals = df.groupby('Team')['Goals'].sum()

# 📊 Graph 1: Goals by Player
player_goals.plot(kind='bar')
plt.title("Goals by Player")
plt.show()

# 📊 Graph 2: Goals by Team
team_goals.plot(kind='bar')
plt.title("Team Performance")
plt.show()

# 📊 Graph 3: Matches vs Goals
plt.scatter(df['Matches'], df['Goals'])
plt.title("Matches vs Goals")
plt.xlabel("Matches")
plt.ylabel("Goals")
plt.show()

# 🧠 Insights
print("\n--- SPORTS INSIGHTS ---")
print("Top Scorer:", player_goals.idxmax())
print("Best Team:", team_goals.idxmax())