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

# print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))
# print(diagonal_sum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))


# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, 
# where A and B are valid parentheses strings, and + represents string concatenation.  
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not 
# exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition: 
# S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in the 
# primitive decomposition of S.
def remove_outer_parentheses(S):
  output = ""
  ps, start = 0, 0
  for i in range(len(S)):
    if S[i] == "(": ps += 1
    if S[i] == ")": ps -= 1
    if ps == 0: output += S[start + 1:i]; start = i + 1
  return output

# print(remove_outer_parentheses("(()())(())"))
# print(remove_outer_parentheses("(()())(())(()(()))"))
# print(remove_outer_parentheses("()()"))