# We are given a list nums of integers representing a list compressed with 
# run-length encoding. Consider each adjacent pair of elements 
# [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, 
# there are freq elements with value val concatenated in a sublist. Concatenate 
# all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.
def decompress_RLElist(nums):
  output = []
  for i in range(0, len(nums), 2):
    for j in range(nums[i]):
      output.append(nums[i + 1])
  return output

# print(decompress_RLElist([1,2,3,4]))
# print(decompress_RLElist([1,1,2,3]))


# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.
def xor_operation(n, start):
  output = 0
  nums = []
  for i in range(n):
    nums.append(start + 2 * i)
  for num in nums:
    output ^= num
  return output

# print(xor_operation(5, 0))
# print(xor_operation(4, 3))
# print(xor_operation(10, 5))

