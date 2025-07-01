import pandas as pd

data = ["paRth", "alice", "bOb", "charLie", "diana"]

series = pd.Series(data)

print("upper case:\n", series.str.upper())
print("lower case:\n", series.str.lower())
print("Title case:\n", series.str.title()) 
print("lengh of data:\n", series.str.len())
print("count of data:\n", series.count())
print("Does Specific Value Exists:\n", series.str.contains("alice"))