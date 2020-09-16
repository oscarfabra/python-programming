# 922. Sort Array By Parity II
def sort_array_by_parity_II(A):
  even, odd = [], []
  for num in A:
    if num % 2 == 0: even += [num]
    else: odd += [num]
  output = []
  for i in range(len(A)):
    output += [even.pop(0)] if i % 2 == 0 else [odd.pop(0)]
  return output

# print(sort_array_by_parity_II([4,2,5,7]))


# 1237. Find Positive Integer Solution for a Given Equation
# This is the custom function interface.
# You should not implement it, or speculate about its implementation
# class CustomFunction:
#     # Returns f(x, y) for any given positive integers x and y.
#     # Note that f(x, y) is increasing with respect to both x and y.
#     # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
#     def f(self, x, y):
def find_solution(customfunction, z):
  pairs = []
  for x in range(1, 1001):
    for y in range(1, 1001):
      if x <= z and y <= z and customfunction.f(x, y) == z: pairs.append([x, y])
  return pairs


# 1491. Average Salary Excluding the Minimum and Maximum Salary
def average(salary):
  salary.remove(min(salary))
  salary.remove(max(salary))
  return sum(salary) / len(salary)

# print(average([4000,3000,1000,2000]))
# print(average([6000,5000,4000,3000,2000,1000]))
# print(average([8000,9000,2000,3000,6000,1000]))


# 1047. Remove All Adjacent Duplicates In String
def adjacent_duplicates(S):
  for i in range(len(S) - 1):
    if S[i] == S[i + 1]: return i
  return -1

def remove_duplicates(S):
  i = adjacent_duplicates(S)
  while i != -1:
    S = S[:i] + S[i + 2:]
    i = adjacent_duplicates(S)
  return S

# print(remove_duplicates("abbaca"))