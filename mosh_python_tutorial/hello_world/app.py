# pounds = input("Tell me your weight in pounds: ")
# kilos = int(pounds) / 2.205
# print("Your weight in kilograms is " + str(kilos))

# price = 1000000
# has_good_credit = True
# if has_good_credit:
#   down_payment = price * 0.1
# else:
#   down_payment = price * 0.2
# print(f"Down payment: ${down_payment}")

name = "Jennifer"
if len(name) < 3:
  print("Name must be at least 3 characters.")
elif len(name) > 50:
  print("Name can be a maximum of 50 characters.")
else:
  print("Name looks good!")