from datetime import datetime

current_date_time = datetime.now()

date_time_without_microseconds = current_date_time.replace(microsecond=0)

print("Date and time with microseconds:", current_date_time)
print("Date and time without microseconds:", date_time_without_microseconds)
