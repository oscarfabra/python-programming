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


# 1460. Make Two Arrays Equal by Reversing Sub-arrays
def can_be_equal(target, arr):
  for num in target:
    if target.count(num) != arr.count(num): return False
  return True

# print(can_be_equal([1,2,3,4], [2,4,1,3]))
# print(can_be_equal([3,7,9], [3,7,11]))
# print(can_be_equal([1,1,1,1,1], [1,1,1,1,1]))


# 461. Hamming Distance
def hamming_distance(x, y):
  xb = '{0:032b}'.format(x)
  yb = '{0:032b}'.format(y)
  dist = 0
  for i in range(len(xb)):
    if xb[i] != yb[i]: dist += 1
  return dist

# print(hamming_distance(1, 4))


# 942. DI String Match
def di_string_match(S):
  output = []
  i, j = 0, len(S)
  for c in S:
    if c == "I": output += [i]; i += 1
    else: output += [j]; j -= 1
  output += [i]
  return output

# print(di_string_match("IDID"))
# print(di_string_match("III"))
# print(di_string_match("DDI"))


# 933. Number of Recent Calls
import collections
class RecentCounter:
  def __init__(self):
    self.q = collections.deque()

  def ping(self, t):
    self.q.append(t)
    while self.q[0] < t - 3000:
      self.q.popleft()
    return len(self.q)

# obj = RecentCounter()
# print(obj.ping(1))
# print(obj.ping(100))
# print(obj.ping(3001))
# print(obj.ping(3002))


# 590. N-ary Tree Postorder Traversal
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
def postorder(root):
  if root is None: return []
  output = []
  for node in root.children:
    output += postorder(node)
  output += [root.val]
  return output


# 589. N-ary Tree Preorder Traversal
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
def preorder(root):
  if root is None: return []
  output = [root.val]
  for node in root.children:
    output += preorder(node)
  return output


# 977. Squares of a Sorted Array
def sorted_squares(A):
  output = []
  for num in A:
    output += [num ** 2]
  return sorted(output)

# print(sorted_squares([-4,-1,0,3,10]))
# print(sorted_squares([-7,-3,2,3,11]))


# 561. Array Partition I
def array_pair_sum(nums):
  nums.sort()
  total = 0
  for i in range(0, len(nums), 2):
    total += min(nums[i], nums[i + 1])
  return total

# print(array_pair_sum([1,4,3,2]))