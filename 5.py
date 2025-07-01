import pandas as pd

data = {
    "Name": ["Parth", "Alice", "Bob", "Charlie", "Diana"],
    "Rank": [1, 2, 3, 4, 5],
    "Score": [100, 90, 80, 70, 60]
}


df = pd.DataFrame(data, index=["Student1", "Student2", "Student3", "Student4", "Student 5"])
print(df)

for i in df:
    print(i)