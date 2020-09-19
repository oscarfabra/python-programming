# 883. Projection Area of 3D Shapes
def xy_sum(grid):
  total = 0
  for lst in grid:
    for num in lst:
      if num != 0: total += 1
  return total

def xz_sum(grid):
  total = 0
  for i in range(len(grid[0])):
    maxi = 0
    for lst in grid:
      maxi = max(lst[i], maxi)
    total += maxi
  return total

def yz_sum(grid):
  total = 0
  for lst in grid:
    total += max(lst)
  return total

def projection_area(grid):
  return xy_sum(grid) + xz_sum(grid) + yz_sum(grid)

# print(projection_area([[1,2],[3,4]]))
# print(projection_area([[1,0],[0,2]]))
# print(projection_area([[1,1,1],[1,0,1],[1,1,1]]))
# print(projection_area([[2,2,2],[2,1,2],[2,2,2]]))


# 1122. Relative Sort Array
def relative_sort_array(arr1, arr2):
  output = []
  not_found = []
  for num in arr2:
    output += [num] * arr1.count(num)
  for num in arr1:
    if not num in arr2: not_found += [num]
  output += sorted(not_found)
  return output

# print(relative_sort_array([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))


# 893. Groups of Special-Equivalent Strings
def get_odd_chars(ele):
  lst = []
  for i in range(1, len(ele), 2):
    lst += [ele[i]]
  return sorted(lst)

def get_even_chars(ele):
  lst = []
  for i in range(0, len(ele), 2):
    lst += [ele[i]]
  return sorted(lst)

def special_equiv(ele_1, ele_2):
  return get_even_chars(ele_1) == get_even_chars(ele_2) and get_odd_chars(ele_1) == get_odd_chars(ele_2)
    
def special_equiv_group(A, ele):
  group = [ele]
  for string in A:
    if string != ele and special_equiv(string, ele): 
      group += [string]
  return group

def in_group(groups, ele):
  for group in groups:
    if ele in group: return True
  return False
    
def num_special_equiv_groups(A):
  groups = []
  for i in range(len(A)):
    if not in_group(groups, A[i]):
      groups += [special_equiv_group(A, A[i])]
  return len(groups)

# print(num_special_equiv_groups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
# print(num_special_equiv_groups(["abc","acb","bac","bca","cab","cba"]))


# 965. Univalued Binary Tree
def is_unival_tree(root, val):
  if root is None: return True
  if root.val != val: return False
  return is_unival_tree(root.left, val) and is_unival_tree(root.right, val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isUnivalTree(root):
  return is_unival_tree(root, root.val)


# 1022. Sum of Root To Leaf Binary Numbers
def sum_root_to_leaves(root, binary):
  if root is None: return 0
  binary += str(root.val)
  if root.left is None and root.right is None: return int(binary, 2)
  return sum_root_to_leaves(root.left, binary) + sum_root_to_leaves(root.right, binary)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sum_root_to_leaf(root):
  return sum_root_to_leaves(root, "")


# 897. Increasing Order Search Tree
def in_order_BST(root, values):
  if root is None: return
  in_order_BST(root.left, values)
  values += [root.val]
  in_order_BST(root.right, values)
  return values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def increasing_BST(root):
  values = in_order_BST(root, [])
  tn = TreeNode(values[-1])
  for i in range(len(values) - 2, -1, -1):
    tn = TreeNode(values[i], None, tn)
  return tn


# 1160. Find Words That Can Be Formed by Characters
def good_string(word, chars):
  for char in word:
    if word.count(char) > chars.count(char): return False
  return True

def count_characters(words, chars):
  total = 0
  for word in words:
    if good_string(word, chars): total += len(word)
  return total

# print(count_characters(["cat","bt","hat","tree"], "atach"))
# print(count_characters(["hello","world","leetcode"], "welldonehoneyr"))


# 929. Unique Email Addresses
def num_unique_emails(emails):
  uniques = set()
  for email in emails:
    local, domain = email.split("@")
    local = local.split("+")[0]
    local = "".join(local.split("."))
    recipient = "@".join([local, domain])
    uniques.add(recipient)
  return len(uniques)

# print(num_unique_emails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


# 509. Fibonacci Number
def fib(N):
  if N == 0 or N == 1: return N
  return fib(N - 1) + fib(N - 2)

# print(fib(3))
# print(fib(4))
# print(fib(5))