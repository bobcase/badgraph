import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("data_science_job_cleaned.csv")

# Target Distribution by City (Cluttered View)
plt.figure(figsize=(14, 6))
sns.countplot(x='city', hue='target', data=df, order=df['city'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Employment Status by City (Cluttered Graphic)")
plt.xlabel("City")
plt.ylabel("Count")
plt.legend(title="Employment Status", labels=["Employed (0)", "Unemployed (1)"])
plt.show()


# Get the top 15 cities with the most candidates
top_cities = df['city'].value_counts().index[:15]
df_top_cities = df[df['city'].isin(top_cities)]

# Grouped Bar Chart for Employment Status in Top Cities
plt.figure(figsize=(12, 6))
sns.countplot(x='city', hue='target', data=df_top_cities, order=top_cities)
plt.xticks(rotation=45)
plt.title("Employment Status in Top 15 Cities (Improved Graphic)")
plt.xlabel("City")
plt.ylabel("Count")
plt.legend(title="Employment Status", labels=["Employed (0)", "Unemployed (1)"])
plt.show()

# Create a normalized stacked bar chart
city_target_counts = df_top_cities.groupby(['city', 'target']).size().unstack()
city_target_percent = city_target_counts.div(city_target_counts.sum(axis=1), axis=0) * 100

# Plot normalized stacked bar chart
city_target_percent.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='coolwarm', edgecolor='black')
plt.title("Percentage of Unemployed Candidates in Top 15 Cities  (Improved Graphic)")
plt.xlabel("City")
plt.ylabel("Percentage")
plt.legend(title="Employment Status", labels=["Employed (0)", "Unemployed (1)"])
plt.xticks(rotation=45)
plt.show()
