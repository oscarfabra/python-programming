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


# 1582. Special Positions in a Binary Matrix
def special_pos(mat, row, col):
  for i in range(len(mat)):
    if i != row and mat[i][col] != 0: return False
  for j in range(len(mat[row])):
    if j != col and mat[row][j] != 0: return False
  return True

def num_special(mat):
  special = 0
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j] == 1 and special_pos(mat, i, j):
        special += 1
        break
  return special

# print(num_special([[1,0,0],[0,0,1],[1,0,0]]))
# print(num_special([[1,0,0],[0,1,0],[0,0,1]]))
# print(num_special([[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]))
# print(num_special([[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]))


# 1394. Find Lucky Integer in an Array
def find_lucky(arr):
  lucky = []
  for num in arr:
    if num == arr.count(num): lucky += [num]
  if len(lucky) == 0: return -1
  else: return max(lucky)

# print(find_lucky([2,2,3,4]))
# print(find_lucky([1,2,2,3,3,3]))
# print(find_lucky([2,2,2,3,3]))


# 1103. Distribute Candies to People
def distribute_candies(candies, num_people):
  result = [0] * num_people
  i = 1
  pos = 0
  candies -= i
  while candies > 0:
    result[pos % num_people] += i
    i += 1
    pos += 1
    if candies - i <= 0: i = candies; candies = 0
    else: candies -= i
  result[pos % num_people] += i
  return result

# print(distribute_candies(7, 4))
# print(distribute_candies(10, 3))


# 637. Average of Levels in Binary Tree
def count_of_level(root, level):
  if root is None: return 0
  if level == 1: return 1
  return count_of_level(root.left, level - 1) + count_of_level(root.right, level - 1)

def sum_of_level(root, level):
  if root is None: return 0
  if level == 1: return root.val
  return sum_of_level(root.left, level - 1) + sum_of_level(root.right, level - 1)

def height(root):
  if root is None: return 0
  lheight = height(root.left)
  rheight = height(root.right)
  if lheight > rheight: return 1 + lheight
  else: return 1 + rheight

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def average_of_levels(root):
  h = height(root)
  avgs = []
  for level in range(1, h + 1):
    avgs.append(sum_of_level(root, level) / count_of_level(root, level))
  return avgs


# 1185. Day of the Week
def leap_year(year):
  if year % 4 != 0: return False
  elif year % 100 != 0: return True
  elif year % 400 != 0: return False
  else: return True

def get_days_of_month(year, month):
  if month == 1: return 31
  elif month == 2: return 28 if not leap_year(year) else 29
  elif month == 3: return 31
  elif month == 4: return 30
  elif month == 5: return 31
  elif month == 6: return 30
  elif month == 7: return 31
  elif month == 8: return 31
  elif month == 9: return 30
  elif month == 10: return 31
  elif month == 11: return 30
    
def get_days_before_month(year, month):
  days = 0
  for m in range(1, month):
    days += get_days_of_month(year, m)
  return days

def get_days_before_year(year):
  days = 0
  for y in range(1971, year):
    if leap_year(y): days += 366
    else: days += 365
  return days

def day_of_the_week(day, month, year):
  # Given that Jan 1 of 1971 was Friday
  week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  days = 0
  days += get_days_before_year(year)
  days += get_days_before_month(year, month)
  days += day
  return week[(4 + days) % 7]

# print(day_of_the_week(31, 8, 2019))
# print(day_of_the_week(18, 7, 1999))
# print(day_of_the_week(15, 8, 1993))