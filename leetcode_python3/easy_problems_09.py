# 1200. Minimum Absolute Difference
def get_min_abs_diff(arr):
  arr.sort()
  min_abs_diff = max(arr) - min(arr)
  for i in range(len(arr) - 1):
    if arr[i + 1] - arr[i] < min_abs_diff: min_abs_diff = arr[i + 1] - arr[i]
  return min_abs_diff

def minimum_abs_difference(arr):
  pairs = []
  min_abs_diff = get_min_abs_diff(arr)
  for i in range(len(arr) - 1):
    if arr[i + 1] - arr[i] == min_abs_diff: pairs += [[arr[i], arr[i + 1]]]
  return pairs

# print(minimum_abs_difference([4,2,1,3]))
# print(minimum_abs_difference([1,3,6,10,15]))
# print(minimum_abs_difference([3,8,-10,23,19,-4,-14,27]))


# 999. Available Captures for Rook
def can_capture_west(board, row, col):
  j = col - 1
  while j >= 0 and board[row][j] == '.': j -= 1
  if j >= 0 and board[row][j] == 'p': return True
  return False

def can_capture_east(board, row, col):
  j = col + 1
  while j < 8 and board[row][j] == '.': j += 1
  if j < 8 and board[row][j] == 'p': return True
  return False

def can_capture_south(board, row, col):
  i = row + 1
  while i < 8 and board[i][col] == '.': i += 1
  if i < 8 and board[i][col] == 'p': return True
  return False

def can_capture_north(board, row, col):
  i = row - 1
  while i >= 0 and board[i][col] == '.': i -= 1
  if i >= 0 and board[i][col] == 'p': return True
  return False

def find_rook_pos(board):
  for i in range(8):
    for j in range(8):
      if board[i][j] == 'R': return i, j
  return -1, -1

def num_rook_captures(board):
  row, col = find_rook_pos(board)
  return can_capture_north(board, row, col) + can_capture_south(board, row, col) + can_capture_east(board, row, col) + can_capture_west(board, row, col)

# print(num_rook_captures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
# print(num_rook_captures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
# print(num_rook_captures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))


# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def max_depth(root):
  if root is None: return 0
  return 1 + max(max_depth(root.left), max_depth(root.right))


# 1025. Divisor Game
def divisor_game(N):
  moves = 0
  while N > 1:
    N -= 1
    moves += 1
  return moves % 2 == 1

# print(divisor_game(2))
# print(divisor_game(3))


# 824. Goat Latin
def to_goat_latin(S):
  goat = []
  i = 1
  for word in S.split():
    if word[0] in "aeiou" or word[0] in "AEIOU": word += "ma"
    else: word = word[1:] + word[0] + "ma"
    word += "a" * i
    goat += [word]
    i += 1
  return " ".join(goat)

# print(to_goat_latin("I speak Goat Latin"))
# print(to_goat_latin("The quick brown fox jumped over the lazy dog"))


# 1030. Matrix Cells in Distance Order
def all_cells_dist_order(R, C, r0, c0):
  cells = {}
  for i in range(R):
    for j in range(C):
      dist = abs(r0 - i) + abs(c0 - j)
      cells[dist] = cells.get(dist, []) + [[i, j]]
  output = []
  for k, v in sorted(cells.items()):
    output += v
  return output

# print(all_cells_dist_order(1, 2, 0, 0))
# print(all_cells_dist_order(2, 2, 0, 1))
# print(all_cells_dist_order(2, 3, 1, 2))


# 908. Smallest Range I
def choose_x(num, K, mid):
  if num <= mid:
    if mid - num >= K: return K
    else: return mid - num
  else:
    if num - mid >= K: return -K
    else: return mid - num

def smallest_range_I(A, K):
  mid = min(A) + (max(A) - min(A)) // 2
  B = []
  for num in A:
    x = choose_x(num, K, mid)
    B += [num + x]
  return max(B) - min(B)

# print(smallest_range_I([1], 0))
# print(smallest_range_I([0,10], 2))
# print(smallest_range_I([1,3,6], 3))


# 463. Island Perimeter
def sides_surrounded_by_water(grid, R, C, row, col):
  sides = 0
  if row == 0 or grid[row - 1][col] == 0: sides += 1
  if row == R - 1 or grid[row + 1][col] == 0: sides += 1
  if col == C - 1 or grid[row][col + 1] == 0: sides += 1
  if col == 0 or grid[row][col - 1] == 0: sides += 1
  return sides

def island_perimeter(grid):
  p = 0
  R = len(grid)
  C = len(grid[0])
  for i in range(R):
    for j in range(C):
      if grid[i][j] == 1: p += sides_surrounded_by_water(grid, R, C, i, j)
  return p

# print(island_perimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
# print(island_perimeter([[1]]))
# print(island_perimeter([[1,0]]))


# 136. Single Number
def single_number(nums):
  count = {}
  for num in nums:
    count[num] = count.get(num, 0) + 1
  for num, times in count.items():
    if times == 1: return num
  return None

# print(single_number([2,2,1]))
# print(single_number([4,1,2,1,2]))