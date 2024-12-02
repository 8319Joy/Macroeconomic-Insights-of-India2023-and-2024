#!/usr/bin/env python
# coding: utf-8
Features:
Importing and Analyzing Data:
Utilize Pandas for data handling.
Key Macroeconomic Indicators:
GDP growth, Inflation rate, Unemployment rate, and Export-Import data.
Visualizations:
Generate line charts, bar plots, and pie charts for insights.
User Interaction:
Interactive input to filter or focus on specific economic indicators.
# In[1]:


pip install pandas matplotlib seaborn


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data Creation
data = {
    "Year": [2023, 2024],
    "GDP Growth (%)": [6.2, 6.4],
    "Inflation Rate (%)": [5.8, 5.6],
    "Unemployment Rate (%)": [7.2, 6.8],
    "Exports (Billion USD)": [700, 750],
    "Imports (Billion USD)": [650, 680]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Macroeconomic Data (India 2023-2024):")
print(df)

# Generate Charts
plt.figure(figsize=(12, 6))

# GDP Growth and Inflation Rate Comparison
plt.subplot(2, 2, 1)
sns.lineplot(x="Year", y="GDP Growth (%)", data=df, marker="o", label="GDP Growth")
sns.lineplot(x="Year", y="Inflation Rate (%)", data=df, marker="o", label="Inflation Rate")
plt.title("GDP Growth vs Inflation Rate")
plt.xlabel("Year")
plt.ylabel("Percentage")
plt.legend()

# Unemployment Rate
plt.subplot(2, 2, 2)
sns.barplot(x="Year", y="Unemployment Rate (%)", data=df, palette="Blues")
plt.title("Unemployment Rate")
plt.xlabel("Year")
plt.ylabel("Percentage")

# Export-Import Analysis
plt.subplot(2, 2, 3)
plt.plot(df["Year"], df["Exports (Billion USD)"], marker="o", label="Exports", color="green")
plt.plot(df["Year"], df["Imports (Billion USD)"], marker="o", label="Imports", color="red")
plt.title("Exports vs Imports")
plt.xlabel("Year")
plt.ylabel("Billion USD")
plt.legend()

# Export-Import Share in 2024 Pie Chart
plt.subplot(2, 2, 4)
export_import = [df.loc[df['Year'] == 2024, "Exports (Billion USD)"].values[0],
                 df.loc[df['Year'] == 2024, "Imports (Billion USD)"].values[0]]
plt.pie(export_import, labels=["Exports", "Imports"], autopct='%1.1f%%', colors=['green', 'red'])
plt.title("Exports vs Imports Share (2024)")

# Save and Show Plot
plt.tight_layout()
plt.savefig("Indian_Economy_2023_2024.png")
plt.show()


# In[ ]:




