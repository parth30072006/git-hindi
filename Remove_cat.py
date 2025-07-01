import pandas as pd

s = pd.Series(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], dtype = "category")

print(s)

s = s.cat.remove_categories(['f', 'g', 'h'])

print("Updated Series with new categories:", s)