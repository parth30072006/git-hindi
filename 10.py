import pandas as pd

df = pd.DataFrame({"Cat1": list("pqrs"), "Cat2": list("abcd"), "Cat3": list("efgh")}, dtype="category")

print(df)
print(df.dtypes)
 