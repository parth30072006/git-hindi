import pandas as pd

data = ["!parth", "\t\talice\n\n", "!!bob", "charLie\t", "diana"]

series = pd.Series(data)
print(series)
print("\nstrip:\n", series.str.strip())
print("\nlstrip:\n", series.str.lstrip("!\n\t")) #Remove specific characters from the left
print("\nrstrip:\n", series.str.rstrip("!\n\t")) #Remove specific characters