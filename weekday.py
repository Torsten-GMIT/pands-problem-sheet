# Task week 05
# Author: Torsten Kindt

# A program that outputs whether today is a weekday or weekend.

# Solution inspired by
    # https://stackoverflow.com/questions/8380389/how-to-get-day-name-from-datetime
    # https://www.delftstack.com/howto/python/python-datetime-day-of-week
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


import datetime
now = datetime.datetime.now()
today = now.strftime("%A")


if today != "Sunday" or "Sunday":
    print("Today is", today,"- yes, unfortunately today is a weekday.")
else:
    print("Today is", today,"- it is the weekend, yay!")




