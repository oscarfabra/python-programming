# 1502. Can Make Arithmetic Progression From Sequence
def can_make_arithmetic_progression(arr):
  arr.sort()
  diff = arr[1] - arr[0]
  for i in range(1, len(arr)):
    if arr[i] - arr[i - 1] != diff: return False
  return True

# print(can_make_arithmetic_progression([3,5,1]))
# print(can_make_arithmetic_progression([1,2,4]))


# 1207. Unique Number of Occurrences
def unique_occurrences(arr):
  count = {}
  for num in arr:
    count[num] = count.get(num, 0) + 1
  return len(set(count.values())) == len(set(arr))

# print(unique_occurrences([1,2,2,1,1,3]))
# print(unique_occurrences([1,2]))
# print(unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]))


# 852. Peak Index in a Mountain Array
def peak_index_in_mountain_array(arr):
  for i in range(1, len(arr) - 1):
    if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]: return i
  return None

# print(peak_index_in_mountain_array([0,10,5,2]))
# print(peak_index_in_mountain_array([3,4,5,1]))
# print(peak_index_in_mountain_array([24,69,100,99,79,78,67,36,26,19]))


# 1051. Height Checker
def height_checker(heights):
  total = 0
  target = sorted(heights)
  for i in range(len(heights)):
    if heights[i] != target[i]: total += 1
  return total

# print(height_checker([1,1,4,2,1,3]))
# print(height_checker([5,1,2,3,4]))
# print(height_checker([1,2,3,4,5]))


# 1380. Lucky Numbers in a Matrix
def lucky_number(matrix, row, col):
  for num in matrix[row]:
    if num < matrix[row][col]: return False
  for i in range(len(matrix)):
    if matrix[i][col] > matrix[row][col]: return False
  return True

def lucky_numbers(matrix):
  output = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if lucky_number(matrix, i, j): output += [matrix[i][j]]
  return output

# print(lucky_numbers([[3,7,8],[9,11,13],[15,16,17]]))
# print(lucky_numbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
# print(lucky_numbers([[7,8],[1,2]]))


# 1403. Minimum Subsequence in Non-Increasing Order
def min_subsequence(nums):
  output = []
  nums.sort(reverse = True)
  while sum(output) <= sum(nums):
    output += [nums.pop(0)]
  return output

# print(min_subsequence([4,3,10,9,8]))
# print(min_subsequence([4,4,7,6,7]))
# print(min_subsequence([6]))


# 557. Reverse Words in a String III
def reverse_words(s):
  lst = s.split()
  new_lst = []
  for word in lst: new_lst += [word[::-1]]
  return " ".join(new_lst)

# print(reverse_words("Let's take LeetCode contest"))


# 944. Delete Columns to Make Sorted
def column_ordered(A, col):
  for i in range(1, len(A)):
    if A[i - 1][col] > A[i][col]: return False
  return True

def min_deletion_size(A):
  D = set()
  for i in range(len(A[0])):
    if not column_ordered(A, i): D.add(i)
  return len(D)

# print(min_deletion_size(["cba","daf","ghi"]))
# print(min_deletion_size(["a","b"]))
# print(min_deletion_size(["zyx","wvu","tsr"]))


# 811. Subdomain Visit Count
def get_subdomains(domain):
  sdomains = []
  pieces = domain.split(".")
  sdomain = ""
  for i in range(len(pieces) - 1, -1, -1):
    if sdomain == "": sdomain = pieces[i]
    else: sdomain = pieces[i] + "." + sdomain
    sdomains += [sdomain]
  return sdomains
    
def subdomain_visits(cpdomains):
  count = {}
  for cpdomain in cpdomains:
    num, domain = cpdomain.split()
    visits = int(num)
    sdomains = get_subdomains(domain)
    for sdomain in sdomains:
      count[sdomain] = count.get(sdomain, 0) + visits
  output = []
  for sdomain, visits in count.items():
    output += [f"{visits} {sdomain}"]
  return output

# print(subdomain_visits(["9001 discuss.leetcode.com"]))
# print(subdomain_visits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))