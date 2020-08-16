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

# Computes the pay given the hours and rate in float type
def compute_pay(hours, rate):
  if hours > 40:
    extra = hours - 40
    return 40 * rate + extra * (rate * 1.5)
  else:
    return hours * rate

print("Pay:", compute_pay(hours, rate))