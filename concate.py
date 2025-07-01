import pandas as pd

data1 = {
    "Name": ["Parth", "Alice", "Bob"],
    "Rank": [1, 2, 3],
    "Score": [100, 90, 80]
}
data2 = {
    "Name": ["Charlie", "Diana" , "Eva"],
    "Rank": [4, 5, 6],
    "Score": [70, 60, 50]
}

dataFrame1 = pd.DataFrame(data1, index=["Student1", "Student2", "Student3"])
dataFrame2 = pd.DataFrame(data2, index=["Student4", "Student5", "Student6"])
 
print(pd.concat([dataFrame1, dataFrame2]))
