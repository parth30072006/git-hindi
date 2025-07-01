import pandas as pd

timestamp = pd.Timestamp(year=2023, month=10, day=1, hour=12)

print("date and Time:", timestamp)
print("\nDay of year:\n", timestamp.dayofyear)