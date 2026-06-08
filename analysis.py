import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/species.csv")

# Display Dataset
print("Dataset:")
print(df)

# Category Analysis
print("\nCategory Counts:")
print(df["Category"].value_counts())

# Bar Chart
plt.figure(figsize=(8,5))
df["Category"].value_counts().plot(kind="bar")

plt.title("Species Conservation Status")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()

# Trend Analysis
yearly = df.groupby("Year").size()

plt.figure(figsize=(8,5))
yearly.plot(marker='o')

plt.title("Species Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Species")

plt.grid(True)

plt.show()