# Reads through a mail log, build a histogram using a dictionary to count how 
# many messages have come from each email address, and print the dictionary.
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
  counts[words[1]] = counts.get(words[1], 0) + 1

print(counts)