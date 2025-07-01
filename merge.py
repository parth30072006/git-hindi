import pandas as pd

data1 = {
    "Name": ["Parth", "Alice", "Bob", "Charlie", "Diana" , "Eva"],
    "Rank": [1, 2, 3, 4, 5 , 6],
    "Score": [100, 90, 80, 70, 60 , 50]
}

data2 ={
    "Id": [101, 102, 103, 104, 105, 106],
    "Roll No": [1, 2, 3, 4, 5, 6]
}

dataFrame1 = pd.DataFrame(data1)

dataFrame2 = pd.DataFrame(data2)


df = dataFrame1.join(dataFrame2)
print(df)