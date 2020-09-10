# 832. Given a binary matrix A, we want to flip the image horizontally, 
# then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed. 
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is 
# replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
def flip_and_invert_image(A):
  for row in A: row.reverse()
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] = 1 if A[i][j] == 0 else 0
  return A

# print(flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]))
# print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))


# 1304. Given an integer n, return any array containing n unique integers such 
# that they add up to 0.
def sum_zero(n):
  output = []
  if n % 2 == 1: output.append(0)
  i = 1
  while len(output) < n: output.append(-i); output.append(i); i += 1
  return output

# print(sum_zero(5))
# print(sum_zero(3))
# print(sum_zero(1))


# 1374. Generate a String With Characters That Have Odd Counts
def generate_the_string(n):
  if n % 2 == 1: return "a" * n
  else: return "a" * (n - 1) + "b"

# print(generate_the_string(4))
# print(generate_the_string(2))
# print(generate_the_string(7))


# 1370. Increasing Decreasing String
def sort_string(s):
  lst = sorted(s)
  result = ""
  while len(lst) > 0:
    result += lst.pop(0)
    i = 0
    while i < len(lst):
      while i < len(lst) and lst[i] == result[-1]: i += 1 
      if i < len(lst): result += lst.pop(i)
    if len(lst) > 0: result += lst.pop(-1)
    i = len(lst) - 1
    while i >= 0:
      while i >= 0 and lst[i] == result[-1]: i -= 1
      if i >= 0: result += lst.pop(i); i -= 1
  return result

# print(sort_string("aaaabbbbcccc"))
# print(sort_string("rat"))
# print(sort_string("leetcode"))
# print(sort_string("ggggggg"))


# 1475. Final Prices With a Special Discount in a Shop
def final_prices(prices):
  output = []
  for i in range(len(prices) - 1):
    j = i + 1
    while j < len(prices) and prices[j] > prices[i]: j += 1
    output += [prices[i] - prices[j]] if j < len(prices) else [prices[i]]
  output += [prices[-1]]
  return output

# print(final_prices([8,4,6,2,3]))
# print(final_prices([1,2,3,4,5]))
# print(final_prices([10,1,1,6]))


# 1299. Replace Elements with Greatest Element on Right Side
def replace_elements(arr):
  output = []
  for i in range(len(arr) - 1):
    output += [max(arr[i + 1:])]
  output += [-1]
  return output

# print(replace_elements([17,18,5,4,6,1]))


# 905. Sort Array By Parity
def sort_array_by_parity(A):
  even, odd = [], []
  for num in A:
    if num % 2 == 0: even += [num]
    else: odd += [num]
  return even + odd

# print(sort_array_by_parity([3,1,2,4]))