hours_str = input("Enter Hours: ")
rate_str = input("Enter Rate: ")
hours = float(hours_str)
rate = float(rate_str)
if hours > 40:
  extra = hours - 40
  pay = 40 * rate + extra * (rate * 1.5)
else:
  pay = hours * rate
print("Pay:", pay)