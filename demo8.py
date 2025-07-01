import pandas as pd

data = {
    "Name": ["Parth", "Alice", "Bob", "Charlie", "Diana" , "Eva"],
    "Rank": [1, 2, 3, 4, 5 , 6],
    "Score": [100, 90, 80, 70, 60 , 50]
}


df = pd.DataFrame(data, index=["Student1", "Student2", "Student3", "Student4", "Student5", "Student6"])
print(df)

print(df.tail(2))