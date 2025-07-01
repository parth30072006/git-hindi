import pandas as pd

timestamp = pd.Timestamp(year=2020, month=9, day=1, hour=12)

print("date and Time:", timestamp)
print("\nis this lip year:\n", timestamp.is_leap_year) 