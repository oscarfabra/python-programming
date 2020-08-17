# For each line, split the line into a list of words using the split function. 
# For each word, check to see if the word is already in a list. If the word is 
# not in the list, add it to the list. When the program completes, sort and 
# print the resulting words in alphabetical order.
file_name = input("Enter a file name: ")
try:
  f_hand = open(file_name)
except:
  print("File cannot be opened:", file_name)
  exit()

my_list = []
for line in f_hand:
  words = line.split()
  for word in words:
    if word not in my_list: my_list.append(word)

my_list.sort()
print(my_list)