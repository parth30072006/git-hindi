import pandas as pd

runs = {
    "Rohit": [100, 50, 75, 80, 90],
    "Virat": [90, 85, 95, 100, 80],
    "Dhoni": [70, 60, 80, 75, 65]
}

df = pd.DataFrame(runs) 
print(df) 
#statistics functions
print("\nsum of:\n", df.sum())
print("\ncount:\n", df.count())
print("\nmaximum runs:\n", df.max())
print("\nmanimum runs:\n", df.min())
print("\nmean:\n", df.mean())
print("\nmedian:\n", df.median())
print("\nStandard Devition:\n", df.std())
print("\nsummery:\n", df.describe())