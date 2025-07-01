import pandas as pd

data = {
    "Name": ["Parth", "Alice", "Bob", "Charlie", "Diana"],
    "Rank": [1, 2, 3, 4, 5],
    "Score": [100, 90, 80, 70, 60]
}


df = pd.DataFrame(data, index=["RowA", "RowB", "RowC", "RowD", "RowE"])
print(df)

print(df.iloc[4,1])