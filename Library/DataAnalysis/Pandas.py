import pandas as pd

# Creating DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
df['Age']  # Selects the Age column
df[df['Age'] > 30]  # Returns rows where Age > 30
df['Country'] = ['USA', 'USA', 'USA']  # Adds a new column
df.drop('Country', axis=1, inplace=True)  # Drops the 'Country' column
df.drop('City', axis=1, inplace=True) 
print(df)