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