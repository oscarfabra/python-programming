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