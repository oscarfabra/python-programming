# 700. Search in a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def search_BST(root, val):
  if root is None:
    return None
  elif root.val == val:
    return root
  else:
    return search_BST(root.left, val) or search_BST(root.right, val)


# 657. Robot Return to Origin
def judge_circle(moves):
  x, y = (0, 0)
  for move in moves:
      if move == "R": x += 1
      elif move == "L": x -= 1
      elif move == "U": y += 1
      else: y -= 1
  return x == 0 and y == 0

# print(judge_circle("UD"))
# print(judge_circle("LL"))
# print(judge_circle("RRDD"))