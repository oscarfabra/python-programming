# We are given a list nums of integers representing a list compressed with 
# run-length encoding. Consider each adjacent pair of elements 
# [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, 
# there are freq elements with value val concatenated in a sublist. Concatenate 
# all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.
def decompress_RLElist(nums):
  output = []
  for i in range(0, len(nums), 2):
    for j in range(nums[i]):
      output.append(nums[i + 1])
  return output

# print(decompress_RLElist([1,2,3,4]))
# print(decompress_RLElist([1,1,2,3]))


# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.
def xor_operation(n, start):
  output = 0
  nums = []
  for i in range(n):
    nums.append(start + 2 * i)
  for num in nums:
    output ^= num
  return output

# print(xor_operation(5, 0))
# print(xor_operation(4, 3))
# print(xor_operation(10, 5))


# Given two arrays of integers nums and index. Your task is to create target 
# array under the following rules:
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the 
# value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and 
# index.
# Return the target array.
# It is guaranteed that the insertion operations will be valid.
def create_target_array(nums, index):
  target = []
  for i in range(len(nums)):
    target.insert(index[i], nums[i])
  return target

# print(create_target_array([0,1,2,3,4], [0,1,2,2,1]))
# print(create_target_array([1,2,3,4,0], [0,1,2,3,0]))


# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.
def balanced_string_split(s):
  total, rs, ls = 0, 0, 0
  for c in s:
    if c == "R": rs += 1
    if c == "L": ls += 1
    if rs == ls:
      total += 1
      rs, ls = 0, 0
  return total

# print(balanced_string_split("RLRRLLRLRL"))
# print(balanced_string_split("RLLLLRRRLR"))
# print(balanced_string_split("LLLLRRRR"))


# Given the root node of a binary search tree, return the sum of values of all 
# nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def range_sum_BST(root, L, R):
  if root is None: return 0
  if root.val < L: return range_sum_BST(root.right, L, R)
  if root.val > R: return range_sum_BST(root.left, L, R)
  return root.val + range_sum_BST(root.left, L, R) + range_sum_BST(root.right, L, R)


# Given an array nums of integers, return how many of them contain an even 
# number of digits.
def find_numbers(nums):
  total = 0
  for num in nums:
    if len(str(num)) % 2 == 0: total += 1
  return total

# print(find_numbers([12,345,2,6,7896]))
# print(find_numbers([555,901,482,1771]))


# Given head which is a reference node to a singly-linked list. The value of 
# each node in the linked list is either 0 or 1. The linked list holds the 
# binary representation of a number.
# Return the decimal value of the number in the linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def get_decimal_value(head):
  s = ""
  while head is not None:
    s += str(head.val)
    head = head.next
  return int(s, 2)