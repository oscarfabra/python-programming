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