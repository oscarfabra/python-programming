# Returns the key given the week day
def get_key_by_week_day(week_day, week_days):
  for key, day in week_days.items():
    if week_day.capitalize() == day: return key
  return -1


# Returns a string with the finish week day given the start week day and the
# number of days later
def get_finish_week_day_str(start_week_day, days_later):
  finish_week_day = ", "
  week_days = {
      0: "Sunday",
      1: "Monday",
      2: "Tuesday",
      3: "Wednesday",
      4: "Thursday",
      5: "Friday",
      6: "Saturday"
    }
  start_key = get_key_by_week_day(start_week_day, week_days)
  finish_key = (start_key + days_later) % 7
  finish_week_day += week_days[finish_key]
  return finish_week_day

# print(get_finish_week_day_str("saturDay", 1))
# print(get_finish_week_day_str("Wednesday", 2))
# print(get_finish_week_day_str("tuesday", 20))


# Returns a string with the finish time given the finish_total_minutes
def get_finish_time_str(finish_total_minutes):
  finish_time = ""
  finish_period = "AM" if finish_total_minutes < 720 else "PM"
  finish_hour = (finish_total_minutes // 60) % 12
  if finish_hour == 0: finish_hour = 12
  finish_time += str(finish_hour) + ":"
  finish_minutes = finish_total_minutes % 60
  finish_time += str(finish_minutes) if finish_minutes >= 10 else "0" + str(finish_minutes)
  finish_time += " " + finish_period
  return finish_time


# Gets the duration time in minutes with the given duration time string
def get_duration_time_in_minutes(duration):
  duration_hours, duration_minutes = duration.split(":")
  return int(duration_hours) * 60 + int(duration_minutes)


# Gets the start time in minutes with the given start time string
def get_start_time_in_minutes(start):
  start_total_minutes = 0
  start_time, start_period = start.split()
  start_hour, start_minutes = start_time.split(":")
  start_total_minutes += int(start_hour) * 60 + int(start_minutes)
  if start_period == "PM": start_total_minutes += 720
  return start_total_minutes


# Adds the duration time to the start time and returns the result according to
# the specifications given in README.md
def add_time(start, duration, week_day = None):
  new_time = ""
  
  start_total_minutes = get_start_time_in_minutes(start)
  duration_total_minutes = get_duration_time_in_minutes(duration)
  finish_total_minutes = (start_total_minutes + duration_total_minutes) % 1440
  new_time += get_finish_time_str(finish_total_minutes)
  
  days_later = (start_total_minutes + duration_total_minutes) // 1440
  if week_day is not None: new_time += get_finish_week_day_str(week_day, days_later)
  if days_later > 0: new_time += " (next day)" if days_later == 1 else f" ({days_later} days later)"

  return new_time

# print(add_time("9:15 PM", "5:30"))
# print(add_time("11:40 AM", "0:25"))
# print(add_time("2:59 AM", "24:00"))
# print(add_time("11:59 PM", "24:05"))
# print(add_time("8:16 PM", "466:02"))
# print(add_time("5:01 AM", "0:00"))
# print(add_time("3:30 PM", "2:12", "Monday"))
# print(add_time("2:59 AM", "24:00", "saturDay"))
# print(add_time("11:59 PM", "24:05", "Wednesday"))
# print(add_time("8:16 PM", "466:02", "tuesday"))