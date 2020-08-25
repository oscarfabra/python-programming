import utils
from ecommerce import shipping
import random
from pathlib import Path

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


# name = "Jennifer"
# if len(name) < 3:
#   print("Name must be at least 3 characters.")
# elif len(name) > 50:
#   print("Name can be a maximum of 50 characters.")
# else:
#   print("Name looks good!")


# prices = [10, 20, 30]
# total = 0
# for price in prices:
#   total += price
# print(f"Total: {total}")


# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#   str = ""
#   for count in range(x_count):
#     str += "x"
#   print(str)


# numbers = [3, 7, 9, 4, 5]
# largest = None
# for num in numbers:
#   if largest is None or num > largest: largest = num
# print(largest)


# numbers = [5, 3, 8, 2, 8, 4, 4, 4, 5, 5, 7]
# for num in numbers:
#   if numbers.count(num) > 1: numbers.remove(num)
# print(numbers)


# numbers = {
#   1: "One",
#   2: "Two",
#   3: "Three",
#   4: "Four",
#   5: "Five",
#   6: "Six",
#   7: "Seven",
#   8: "Eight",
#   9: "Nine"
# }
# phone = input("Phone: ")
# str = ""
# for digit in phone:
#   str += numbers[int(digit)] + " "
# print(str)


# numbers = [10, 3, 6, 2, 7]
# print(utils.find_max(numbers))
# shipping.calc_shipping()


# members = ["John", "Mary", "Bob", "Oscar"]
# leader = random.choice(members)
# print(leader)


path = Path()
for file in path.glob("*"):
  print(file)