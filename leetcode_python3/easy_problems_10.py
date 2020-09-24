# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
def is_prefix_of_word(sentence, searchWord):
  i = 1
  for word in sentence.split():
    if word.find(searchWord) == 0: return i
    i += 1
  return -1

# print(is_prefix_of_word("i love eating burger", "burg"))
# print(is_prefix_of_word("this problem is an easy problem", "pro"))
# print(is_prefix_of_word("i use triple pillow", "pill"))
# print(is_prefix_of_word("hello from the other side", "they"))


# 766. Toeplitz Matrix
def diag_has_same_ele(matrix, ele, row, col, R, C):
  i, j = row, col
  while i < R and j < C:
    if matrix[i][j] != ele: return False
    i += 1
    j += 1
  return True
        
def is_toeplitz_matrix(matrix):
  R = len(matrix)
  C = len(matrix[0])
  for i in range(R):
    if not diag_has_same_ele(matrix, matrix[i][0], i, 0, R, C): return False
  for j in range(1, C):
    if not diag_has_same_ele(matrix, matrix[0][j], 0, j, R, C): return False
  return True

# print(is_toeplitz_matrix([
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]))
# print(is_toeplitz_matrix([
#   [1,2],
#   [2,2]
# ]))


# 1399. Count Largest Group
def sum_of_digits(num):
  total = 0
  while num > 0:
    total += num % 10
    num //= 10
  return total

def count_largest_group(n):
  groups = {}
  for i in range(1, n + 1):
    s = sum_of_digits(i)
    groups[s] = groups.get(s, []) + [i]
  max_len = 0
  for lst in groups.values():
    max_len = max(max_len, len(lst))
  largest = 0
  for lst in groups.values():
    if len(lst) == max_len: largest += 1
  return largest

# print(count_largest_group(13))
# print(count_largest_group(15))
# print(count_largest_group(24))


# 806. Number of Lines To Write String
def number_of_lines(widths, S):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  lines = 1
  units = 0
  for c in S:
    units += widths[alpha.index(c)]
    if units > 100:
      units = widths[alpha.index(c)]
      lines += 1
  return [lines, units]

# print(number_of_lines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
# print(number_of_lines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))


# 1413. Minimum Value to Get Positive Step by Step Sum
def min_start_value(nums):
  start_value = 1
  while (True):
    i = 0
    total = start_value
    while i < len(nums):
      total += nums[i]
      if total < 1: break
      i += 1
    if i == len(nums): return start_value
    start_value += 1

# print(min_start_value([-3,2,-3,4,2]))
# print(min_start_value([1,2]))
# print(min_start_value([1,-2,-3]))


# 500. Keyboard Row
def word_in_row(word, row):
  for c in word:
    if c.lower() not in row: return False
  return True

def find_words(words):
  rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
  result = []
  for word in words:
    for row in rows:
      if word_in_row(word, row): result += [word]; break
  return result

# print(find_words(["Hello", "Alaska", "Dad", "Peace"]))


# 476. Number Complement
def flip_bits(binary):
  result = ""
  for bit in binary:
    result += "0" if bit == "1" else "1"
  return result

def find_complement(num):
  num_bin = "{0:016b}".format(num)
  num_bin = num_bin.lstrip("0")
  comp_bin = flip_bits(num_bin)
  return int(comp_bin, 2)

# print(find_complement(5))
# print(find_complement(1))
# print(find_complement(123))


# 1217. Minimum Cost to Move Chips to The Same Position
def min_cost_to_move_chips(position):
  evens = 0
  for pos in position:
    if pos % 2 == 0: evens += 1
  odds = len(position) - evens
  if evens >= odds: return odds
  else: return evens

# print(min_cost_to_move_chips([1,2,3]))
# print(min_cost_to_move_chips([2,2,2,3,3]))
# print(min_cost_to_move_chips([1,1000000000]))


# 237. Delete Node in a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def delete_node(node):
  """
  :type node: ListNode
  :rtype: void Do not return anything, modify node in-place instead.
  """
  node.val = node.next.val
  node.next = node.next.next