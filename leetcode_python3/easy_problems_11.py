# 872. Leaf-Similar Trees
def get_leaves(root, leaves):
  if root is None: return
  if root.left is None and root.right is None: leaves.append(root.val); return
  get_leaves(root.left, leaves)
  get_leaves(root.right, leaves)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def leafSimilar(root1, root2):
  leaves1 = []
  leaves2 = []
  get_leaves(root1, leaves1)
  get_leaves(root2, leaves2)
  return leaves1 == leaves2


# 682. Baseball Game
def cal_points(ops):
  valid = []
  for op in ops:
    if op.replace("-", "").isdigit():
      valid += [int(op)]
    elif op == 'C':
      valid.pop(-1)
    elif op == 'D':
      valid += [2 * valid[-1]]
    else:
      valid += [valid[-1] + valid[-2]]
  return sum(valid)

# print(cal_points(["5","2","C","D","+"]))
# print(cal_points(["5","-2","4","C","D","9","+","+"]))


# 496. Next Greater Element I
def next_greater_element(nums1, nums2):
  result = []
  for num in nums1:
    ngn = -1
    for i in range(nums2.index(num), len(nums2)):
      if nums2[i] > num: ngn = nums2[i]; break
    result += [ngn]
  return result

# print(next_greater_element([4,1,2], [1,3,4,2]))
# print(next_greater_element([2,4], [1,2,3,4]))


# 705. Design HashSet
class MyHashSet:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.values = set()

  def add(self, key: int) -> None:
    self.values.add(key)

  def remove(self, key: int) -> None:
    self.values.discard(key)

  def contains(self, key: int) -> bool:
    """
    Returns true if this set contains the specified element
    """
    return key in self.values

# hash_set = MyHashSet()
# hash_set.add(1)         
# hash_set.add(2)         
# print(hash_set.contains(1))    # returns true
# print(hash_set.contains(3))    # returns false (not found)
# hash_set.add(2)          
# print(hash_set.contains(2))    # returns true
# hash_set.remove(2)          
# print(hash_set.contains(2))    # returns false (already removed)