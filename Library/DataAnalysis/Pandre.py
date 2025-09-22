# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# Load the Iris dataset
try:
    iris = load_iris()
    # Convert to pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())
# Set seaborn style for better visuals
sns.set(style="whitegrid")

# 1. Line Chart: Petal Length Trend (assuming ordered by index as pseudo-time)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['petal length (cm)'], label='Petal Length', color='blue')
plt.title('Petal Length Trend Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# 2. Bar Chart: Average Petal Length by Species
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean', hue='species', palette='viridis')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# 3. Histogram: Distribution of Sepal Length
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True, color='green')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', size='species', data=df, palette='deep')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
