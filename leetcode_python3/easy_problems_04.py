# 832. Given a binary matrix A, we want to flip the image horizontally, 
# then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed. 
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is 
# replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
def flip_and_invert_image(A):
  for row in A: row.reverse()
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] = 1 if A[i][j] == 0 else 0
  return A

# print(flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]))
# print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))


# 1304. Given an integer n, return any array containing n unique integers such 
# that they add up to 0.
def sum_zero(n):
  output = []
  if n % 2 == 1: output.append(0)
  i = 1
  while len(output) < n: output.append(-i); output.append(i); i += 1
  return output

# print(sum_zero(5))
# print(sum_zero(3))
# print(sum_zero(1))