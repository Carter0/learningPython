#!/usr/local/bin/python3

# Me messing around with time in Python.
# Also me messing around with datetime.

import time
import datetime
import pytz

# This gets the local time.
# This will return a named tuple with 9 fields.
# Most of those fields are parts of time like seconds, days, months, years etc...
t = time.localtime()

# This will output the epoch time. Which does differ depending on the platform.
# Epoch time is the amount of seconds since a certain point in time.
# For Unix, it started in 1970.
# Slack API uses epoch time so it useful to have.
epoch_time = time.mktime(t)

# ---------------------------- DateTime stuff now

# Doing this makes the day, month, and year attibutes of the class.
birthday = datetime.date(1997, 1, 9)
# Note* just doing print(date) will output it in a decently nice format already
print("My Birthday is {}, {}, {}".format(date.day, date.month, date.year))

# Now getting time
# Similar to how date works.
midday = datetime.time(12, 30, 30)
print(midday)

# This just combines both of the above.
datetime = datetime.datetime(1997, 1, 9, 12, 30, 30)


# Getting the current date
today = date.today()
# Will output a number. 0 being Monday, 6 being Sunday.
today.weekday()
# Will output a number. 1 being Monday, 7 being Sunday.
today.isoweekday()
# This will return the same tuple that localtime() for the time module outputs.
print(today.timetuple())

# You can even do some arithmetic with dates.
# This outputs a timedelta, which can be used in many different ways.
dif = today - birthday
#  Will print the difference in days.
print(dif)


# Messing around with timedelta Some more.
# Note, time delta is basically the difference between datetimes

d = timedelta(days=7)
# Will print out the current date + one week
print("One week from today is: {}".format(today + d))

# Now I want to deal with timezones

# Line below defaults to the correct timezone for me (EST).
# I don't know how it does this but I assume the default argument for timezone is EST.
today = datetime.now()

# In order to get more detailed information on timezones, I intalled the pytz module.
# This gets an aware timezone object, unlike all the other objects, which were naive.
dt_utcnow = datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# Getting a specific datetime
dt_EST = datetime.now(tz=pytz.timezone('US/Eastern'))
print("The aware eastern standard time is {}".format(dt_EST))







