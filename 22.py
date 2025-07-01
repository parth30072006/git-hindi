import pandas as pd

timestamp = pd.Timestamp(year=2023, month=9, day=1, hour=12)

print("date and Time:", timestamp)
print("\nDay in month:\n", timestamp.daysinmonth)