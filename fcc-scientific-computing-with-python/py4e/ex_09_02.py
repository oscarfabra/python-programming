# Categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third 
# word and keep a running count of each of the days of the week. At the end 
# of the program print out the contents of your dictionary (order does not 
# matter).
file_name = input("Enter a file name: ")
try:
  f_hand = open(file_name)
except:
  print("File cannot be opened:", file_name)
  exit()

counts = {}
for line in f_hand:
  words = line.split()
  if len(words) < 3 or words[0] != "From": continue
  counts[words[2]] = counts.get(words[2], 0) + 1

print(counts)