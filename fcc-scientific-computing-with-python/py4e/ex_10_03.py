# Reads a file and prints the letters in decreasing order of frequency. Your 
# program should convert all the input to lower case and only count the letters 
# a-z. Your program should not count spaces, digits, punctuation, or anything 
# other than the letters a-z.
file_name = input("Enter a file name: ")
try:
  f_hand = open(file_name)
except:
  print("File cannot be opened:", file_name)
  exit()

counts = {}
for line in f_hand:
  letters = list(line.rstrip())
  for c in letters:
    if c.isalpha(): counts[c.lower()] = counts.get(c.lower(), 0) + 1

tuples = sorted([ (count, letter) for letter, count in counts.items() ], reverse = True)

for count, letter in tuples:
  print(letter, count)
