import pandas as pd

data = {
    'Id' : ['S01', 'S02', 'S03', 'S04', 'S05', 'S06'],
    'Name' : ["Dhoni", "Starc", "Kane", "Stokes", "Phillips", "Ricky"],
    'Position' : ["Batsman", "Bowler", "Batsman", "All-rounder", "All-rounder", "Batsman"],
    'Runs' : [100, 20, 15, 118, 220, 300],
    'country' : ["India", "Australia", "New Zealand", "England", "New Zealand", "Australia"]
} 

df = pd.DataFrame(data)

print(df)

print("Selecting columns in Range :\n", df[df.columns[1:3]])