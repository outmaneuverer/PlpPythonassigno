import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [23, 30, 35, 29, 40]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot as a bar chart
plt.bar(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name vs Age')
plt.xticks(rotation=45)
plt.show()
