# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the 
# elements on the secondary diagonal that are not part of the primary diagonal.
def diagonal_sum(mat):
  total = 0
  for i in range(len(mat)):
    if not (len(mat) % 2 == 1 and len(mat) // 2 == i): total += mat[i][i]
  for i in range(len(mat)):
    total += mat[i][-1 - i]
  return total

print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))
print(diagonal_sum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))