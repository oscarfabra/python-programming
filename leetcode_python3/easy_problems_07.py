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


# 1337. The K Weakest Rows in a Matrix
def k_weakest_rows(mat, k):
  count = {}
  for i in range(len(mat)): count[i] = sum(mat[i])
  count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
  return list(count.keys())[:k]

# print(k_weakest_rows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))
# print(k_weakest_rows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 2))


# 344. Reverse String
def reverse_string(s):
  """
  Do not return anything, modify s in-place instead.
  """
  n = len(s)
  for i in range(n): s.insert(n - 1 - i, s.pop(0))

# print(reverse_string(["h","e","l","l","o"]))
# print(reverse_string(["H","a","n","n","a","h"]))


# 559. Maximum Depth of N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def max_depth(root):
  if root is None: return 0
  maxi = 0
  for node in root.children:
    maxi = max(maxi, max_depth(node))
  return maxi + 1


# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middle_node(head):
  length = 0
  h = head
  while head is not None:
    head = head.next
    length += 1
  for i in range(length // 2):
    h = h.next
  return h


# 1356. Sort Integers by The Number of 1 Bits
def sort_by_bits(arr):
  count = {}
  for num in arr:
      ones = "{0:016b}".format(num).count('1')
      count[ones] = count.get(ones, []) + [num]
  count = {k: v for k, v in sorted(count.items(), key=lambda item: item[0])}
  output = []
  for bits, nums in count.items():
      output += sorted(nums)
  return output

# print(sort_by_bits([0,1,2,3,4,5,6,7,8]))
# print(sort_by_bits([1024,512,256,128,64,32,16,8,4,2,1]))
# print(sort_by_bits([2,3,5,7,11,13,17,19]))
# print(sort_by_bits([10,100,1000,10000]))


# 1002. Find Common Characters
def min_times_appears(A, char):
  min_times = len(A[0])
  for word in A:
    times = word.count(char)
    if times < min_times: min_times = times
  return min_times

def common_chars(A):
  chars = []
  for c in A[0]:
    n = min_times_appears(A, c)
    if c not in chars and n != 0: 
      chars += [c] * n
  return chars

# print(common_chars(["bella","label","roller"]))
# print(common_chars(["cool","lock","cook"]))