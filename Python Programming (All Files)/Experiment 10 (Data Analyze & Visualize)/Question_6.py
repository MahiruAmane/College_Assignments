# Write a Python Program To Use Pandas To Find & Replace the Missing Values,
# In a Given DataFrame Which Do Not Have Any Valuable Information.

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Marks': [85, pd.NA, 95, 60, 75],
    'Attempts': [1, 2, 3, None, 5]
}

df = pd.DataFrame(data)
print("Before Replacing Missing Values : \n")
print(df)

df['Marks'] = df['Marks'].fillna(int(df['Marks'].mean()))
df['Attempts'] = df['Attempts'].fillna(int(df['Attempts'].median()))

print("\n")
print("After Replacing Missing Values : \n")
print(df)