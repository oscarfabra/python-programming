# Returns the maximum of two numbers
def maximum(a, b):
  return a if a >= b else b

# print(maximum(9, 7))

# If the number is divisible by 3, return "Fizz". If it is divisible by 5, it
# returns "Buzz". If it is divisible by both 3 and 5, returns "FizzBuzz".
# Otherwise it returns the same number.
def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    return num

# print(fizz_buzz(15))
# print(fizz_buzz(9))
# print(fizz_buzz(10))
# print(fizz_buzz(7))

# If speed is less than 70, it prints “Ok”. Otherwise, for every 5km above the
# speed limit (70), it gives the driver one demerit point and prints the total 
# number of demerit points. For example, if the speed is 80, it prints: 
# “Points: 2”.
# If the driver gets more than 12 points, the function prints: 
# “License suspended”
def check_speed(speed):
  if speed < 70:
    print("Ok")
  else:
    points = 0
    while speed > 70:
      points += 1
      speed -= 5
    print("Points:", points) if points <= 12 else print("License suspended")

# check_speed(60)
# check_speed(70)
# check_speed(80)
# check_speed(140)

# Prints all the numbers between 0 and limit with a label to identify the even 
# and odd numbers. For example, if the limit is 3, it prints:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
def showNumbers(limit):
  for i in range(limit + 1):
    print(i, "EVEN") if i % 2 == 0 else print(i, "ODD")

# showNumbers(3)

# Returns the sum of multiples of 3 and 5 between 0 and limit. For example, if 
# limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def sum_of_multiples(limit):
  total = 0
  for i in range(limit + 1):
    if i % 3 == 0 or i % 5 == 0: total += i
  return total

# print(sum_of_multiples(5))
# print(sum_of_multiples(10))
# print(sum_of_multiples(20))

# If rows is 5, it prints the following:
# *
# **
# ***
# ****
# *****
def show_stars(rows):
  for i in range(rows):
    print("*" * (i + 1))

# show_stars(5)

# Prints all the prime numbers between 0 and limit.
def show_primes(limit):
  for i in range(2, limit + 1):
    if is_prime(i): print(i)

# Tells whether the number is prime or not
def is_prime(num):
  if num < 2: return False
  for i in range(2, num // 2 + 1):
    if num % i == 0: return False
  return True

# show_primes(20)