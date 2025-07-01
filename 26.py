import pandas as pd

data = {
    "Player": ["Rohit", "Virat", "Rishabh", "Hardik", "Jasprit", "Aditya"],
    "Runs": [100, 200, 150, 180, 120, 130],
    "Rank": [1, 2, 3, 4, 5, 6 ]
}

df = pd.DataFrame(data)
print("Cricket Players Records:\n", df)

res = df.groupby('Player')

print("\nGrouped by Player:\n", res.first()) 