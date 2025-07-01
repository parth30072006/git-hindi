import pandas as pd

data = {
    'Name' : ["Steve", "Starc", "Josh", "cummins", "Travis", "Ricky"],
    'Position' : ["Batsman", "Bowler", "Bowler", "Bowler", "All-rounder", "Batsman"],
    'Runs' : [100, 20, 15, 18, 220, 300]
} 

df = pd.DataFrame(data, index=["Player1", "Player2", "Player3", "Player4", "Player5", "Player6"])

print(df)

print("Selecting only two columns:\n", df[["Name", "Position"]])