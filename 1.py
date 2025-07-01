import pandas as pd

data = {
    "Name": ["Parth" , "Alice" , "Bob"],
    "Rank": [1 , 2 , 3],
    "Score": [100 , 90 , 80]
}

df = pd.DataFrame(data)
print(df)