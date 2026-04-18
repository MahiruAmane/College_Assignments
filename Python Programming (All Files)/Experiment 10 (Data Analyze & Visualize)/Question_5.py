# Write a Python Program To Use Pandas To Get The First 3 Rows Of a Given DataFrame.

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Marks': [85, 90, 95, 80, 75],
    'Attempts': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)
print(df.head(3))