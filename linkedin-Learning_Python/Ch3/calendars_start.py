#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2019, 1, 0, 0)
# print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2019, 1)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2019, 3):
#   print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for month in calendar.month_name:
#   print(month)

# for day in calendar.day_name:
#   print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on: ")
for month in range(1, 13):
  month_calendar = calendar.monthcalendar(2019, month)
  week_one = month_calendar[0]
  week_two = month_calendar[1]

  meet_day = week_one[calendar.FRIDAY] if week_one[calendar.FRIDAY != 0] else week_two[calendar.FRIDAY]
  print("%10s %2d" % (calendar.month_name[month], meet_day))

