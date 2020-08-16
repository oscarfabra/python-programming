hours_str = input("Enter Hours: ")
try:
  hours = float(hours_str)
except:
  print("Error, please enter numeric input")
  quit()
rate_str = input("Enter Rate: ")
try:
  rate = float(rate_str)
except:
  print("Error, please enter numeric input")
  quit()
if hours > 40:
  extra = hours - 40
  pay = 40 * rate + extra * (rate * 1.5)
else:
  pay = hours * rate
print("Pay:", pay)