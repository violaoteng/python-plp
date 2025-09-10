# Loading and Exploring the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Loading Iris dataset from sklearn
try:
    iris = load_iris(as_frame=True)
    df = iris.frame  # Converting to pandas DataFrame
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Dataset not found. Please check the file path.")
except Exception as e:
    print("An error occurred while loading dataset:", e)

# Display first few rows
print("First 5 rows of the dataset:\n")
print(df.head(), "\n")

# Check dataset structure
print("Dataset Info:\n")
print(df.info(), "\n")

# Check missing values
print("Missing Values:\n")
print(df.isnull().sum(), "\n")

# Clean missing values
df = df.dropna()

# Basic Data Analysis
print("Basic Statistics:\n")
print(df.describe(), "\n")

# Grouping: Mean petal length per species
grouped = df.groupby("target")["petal length (cm)"].mean()
print("Average Petal Length per Species:\n")
print(grouped, "\n")

# Map target integers to actual species names
df["species"] = df["target"].map(dict(zip(range(3), iris.target_names)))

# Data Visualization

# 1. Line chart 
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="Set2")
plt.title("Bar Chart: Avg Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, edgecolor="black")
plt.title("Histogram: Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
