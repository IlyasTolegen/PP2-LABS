from datetime import datetime

date1 = datetime(2023, 10, 24, 12, 30, 0)
date2 = datetime(2023, 10, 25, 14, 45, 30)

difference = date2 - date1

seconds_difference = difference.total_seconds()

print(f"Difference in seconds: {seconds_difference} seconds")
