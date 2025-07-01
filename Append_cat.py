import pandas as pd

s = pd.Series(['a', 'b', 'c', 'd', 'e'], dtype = "category")

print(s)

s = s.cat.add_categories(['f', 'g', 'h'])

print("Updated Series with new categories:", s)