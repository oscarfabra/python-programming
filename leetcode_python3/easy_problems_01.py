# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums. 
def running_sum(nums):
  output = []
  total = 0
  for num in nums:
    total += num
    output.append(total)
  return output

# print(running_sum([1,2,3,4]))
# print(running_sum([1,1,1,1,1]))
# print(running_sum([3,1,2,10,1]))


# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
def shuffle(nums, n):
  output = []
  for i in range(n):
    output += [nums[i]] + [nums[n + i]]
  return output

# print(shuffle([2,5,1,3,4,7], 3))
# print(shuffle([1,2,3,4,4,3,2,1], 4))

# Given the array candies and the integer extraCandies, where candies[i] 
# represents the number of candies that the ith kid has. For each kid check 
# if there is a way to distribute extraCandies among the kids such that he or
# she can have the greatest number of candies among them. Notice that multiple
# kids can have the greatest number of candies.
def kids_with_candies(candies, extra_candies):
  output = []
  max_candies = max(candies)
  for num_candies in candies:
    output += [num_candies + extra_candies >= max_candies]
  return output

# print(kids_with_candies([2,3,5,1,3], 3))
# print(kids_with_candies([4,2,1,1,2], 1))


# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.
def num_identical_pairs(nums):
  pairs = 0
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      if nums[i] == nums[j]: pairs += 1
  return pairs


# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
def defang_IP_addr(address):
  output = ""
  for i in range(len(address)):
    output += "[.]" if address[i] == "." else address[i]
  return output
 

# You're given strings J representing the types of stones that are jewels, 
# and S representing the stones you have.  Each character in S is a type of 
# stone you have.  You want to know how many of the stones you have are also 
# jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are 
# letters. Letters are case sensitive, so "a" is considered a different type 
# of stone from "A".
def num_jewels_in_stones(J, S):
  total = 0
  for i in range(len(S)):
    if S[i] in J: total += 1
  return total


# Given a non-negative integer num, return the number of steps to reduce it to 
# zero. If the current number is even, you have to divide it by 2, otherwise, 
# you have to subtract 1 from it.
def number_of_steps (num):
  steps = 0
  while num != 0:
    num = num / 2 if num % 2 == 0 else num - 1
    steps += 1
  return steps


# Given the array nums, for each nums[i] find out how many numbers in the array 
# are smaller than it. That is, for each nums[i] you have to count the number 
# of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
def smaller_numbers_than_current(nums):
  output = []
  for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
      if j != i and nums[j] < nums[i]: count += 1
    output.append(count)
  return output

# print(smaller_numbers_than_current([8,1,2,2,3]))
# print(smaller_numbers_than_current([6,5,4,8]))


# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position 
# moves to indices[i] in the shuffled string.
# Return the shuffled string.
def restore_string(s, indices):
  output = list(s)
  for i in range(len(indices)):
    output[indices[i]] = s[i]
  return "".join(output)

# print(restore_string("codeleet", [4,5,6,7,0,2,1,3]))
# print(restore_string("aiohn", [3,1,4,2,0]))
# print(restore_string("aaiougrt", [4,0,2,6,7,3,1,5]))


# Given an integer number n, return the difference between the product of its 
# digits and the sum of its digits.
def subtract_product_and_sum(n):
  s = 0
  p = 1
  while n > 0:
    digit = n % 10
    s += digit
    p *= digit
    n //= 10
  return p - s

# print(subtract_product_and_sum(234))
# print(subtract_product_and_sum(4421))