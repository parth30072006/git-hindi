import pandas as pd

timestamp = pd.Timestamp(year=2023, month=12, day=1, hour=12)

print("date and Time:", timestamp)
print("\nis this month end:\n", timestamp.is_month_end)
print("\nis this month start:\n", timestamp.is_month_start)  
print("\nis this year end:\n", timestamp.is_year_end)
print("\nis this year start:\n", timestamp.is_year_start)  