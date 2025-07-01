import pandas as pd

data = {
    'Id' : ['S01', 'S02', 'S03', 'S04', 'S05', 'S06'],
    'Rank' : [6,5,1,2,3,4],
    'Name' : ["Dhoni", "Starc", "Kane", "stokes", "Phillips", "Ricky"],
    'Position' : ["Batsman", "Bowler", "Batsman", "All-rounder", "All-rounder", "Batsman"],
    'Runs' : [100, 20, 15, 118, 220, 300] ,
    'country' : ["India", "Australia", "New Zealand", "England", "New Zealand", "Australia"]
} 

df = pd.DataFrame(data)

print(df)

result = df.drop_duplicates()

print("\n", result)