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


# 1252. Given n and m which are the dimensions of a matrix initialized by zeros 
# and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] 
# you have to increment all cells in row ri and column ci by 1.
# Return the number of cells with odd values in the matrix after applying the 
# increment to all indices.
def odd_cells(n, m, indices):
  mat = [[0 for x in range(m)] for y in range(n)]
  for r, c in indices:
    for i in range(m): mat[r][i] += 1
    for i in range(n): mat[i][c] += 1
  odd = 0
  for i in range(n):
    for j in range(m):
      if mat[i][j] % 2 == 1: odd += 1
  return odd

# print(odd_cells(2, 3, [[0,1],[1,1]]))
# print(odd_cells(2, 2, [[1,1],[0,0]]))


# 1323. Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit 
# (6 becomes 9, and 9 becomes 6).
def maximum_69_number(num):
  s = str(num)
  i = 0
  while i < len(s) and s[i] == "9": i += 1
  if i < len(s): s = s[:i] + "9" + s[i + 1:]
  return int(s)

# print(maximum_69_number(9669))
# print(maximum_69_number(9996))
# print(maximum_69_number(9999))


# 1464. Given the array of integers nums, you will choose two different 
# indices i and j of that array. Return the maximum value of 
# (nums[i]-1)*(nums[j]-1).
def max_product(nums):
  m = 0
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      if (nums[i] - 1) * (nums[j] - 1) > m: 
        m = (nums[i] - 1) * (nums[j] - 1)
  return m

# print(max_product([3,4,5,2]))
# print(max_product([1,5,4,5]))
# print(max_product([3,7]))


# 1450. Given two integer arrays startTime and endTime and given an integer 
# queryTime. The ith student started doing their homework at the time 
# startTime[i] and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime. 
# More formally, return the number of students where queryTime lays in the 
# interval [startTime[i], endTime[i]] inclusive.
def busy_student(startTime, endTime, queryTime):
  total = 0
  for i in range(len(startTime)):
    if queryTime in range(startTime[i], endTime[i] + 1): total += 1
  return total

# print(busy_student([1,2,3], [3,2,7], 4))
# print(busy_student([1,1,1,1], [1,3,2,4], 7))
# print(busy_student([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5))


# 804. International Morse Code defines a standard encoding where each letter is 
# mapped to a series of dots and dashes, as follows: "a" maps to ".-", 
# "b" maps to "-...", "c" maps to "-.-.", and so on.
# Now, given a list of words, each word can be written as a concatenation of the 
# Morse code of each letter. For example, "cab" can be written as "-.-..--...", 
# (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a 
# concatenation, the transformation of a word.
# Return the number of different transformations among all words we have.
def unique_morse_representations(words):
  alpha = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..",
            "e":".", "f":"..-.", "g":"--.", "h":"....",
            "i":"..", "j":".---", "k":"-.-", "l":".-..",
            "m":"--", "n":"-.", "o":"---", "p":".--.",
            "q":"--.-", "r":".-.", "s":"...", "t":"-",
            "u":"..-", "v":"...-", "w":".--", "x":"-..-",
            "y":"-.--", "z":"--.."}
  transformed = []
  for word in words:
    code = ""
    for c in word: code += alpha[c]
    transformed.append(code)
  return len(set(transformed))

# print(unique_morse_representations(["gin", "zen", "gig", "msg"]))


# 1436. You are given the array paths, where paths[i] = [cityAi, cityBi] means 
# there exists a direct path going from cityAi to cityBi. Return the 
# destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, 
# therefore, there will be exactly one destination city.
def dest_city(paths):
  cities = set()
  for a, b in paths: cities.add(a); cities.add(b)
  for city in cities:
    starter_city = False
    for path in paths:
      if path[0] == city: starter_city = True; break
    if not starter_city: return city

# print(dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
# print(dest_city([["B","C"],["D","B"],["C","A"]]))
# print(dest_city([["A","Z"]]))


# 1309. Given a string s formed by digits ('0' - '9') and '#' . We want to 
# map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
# Return the string formed after mapping.
# It's guaranteed that a unique mapping will always exist.
def freq_alphabets(s):
  alpha = {"1": "a", "2":"b", "3":"c", "4":"d", "5":"e",
          "6": "f", "7":"g", "8":"h", "9":"i", "10#":"j",
          "11#": "k", "12#":"l", "13#":"m", "14#":"n", "15#":"o",
          "16#": "p", "17#":"q", "18#":"r", "19#":"s", "20#":"t",
          "21#": "u", "22#":"v", "23#":"w", "24#":"x", "25#":"y", "26#":"z"}
  output = ""
  i = 0
  while i < len(s):
    if i + 2 < len(s) and s[i + 2] == "#": code = s[i:i + 3]; i += 3
    else: code = s[i]; i += 1
    output += alpha[code]
  return output

# print(freq_alphabets("10#11#12"))
# print(freq_alphabets("1326#"))
# print(freq_alphabets("25#"))
# print(freq_alphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))


# 1351. Given a m * n matrix grid which is sorted in non-increasing order both 
# row-wise and column-wise. 
# Return the number of negative numbers in grid.
def count_negatives(grid):
  output = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] < 0: output += 1
  return output

# print(count_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
# print(count_negatives([[3,2],[1,0]]))
# print(count_negatives([[1,-1],[-1,-1]]))