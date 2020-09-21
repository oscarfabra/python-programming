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