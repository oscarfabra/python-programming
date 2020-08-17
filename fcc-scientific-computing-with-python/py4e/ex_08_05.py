# Reads through the mail box data and when you find line that starts with 
# “From”, you will split the line into words using the split function. We are 
# interested in who sent the message, which is the second word on the 
# From line.
file_name = input("Enter a file name: ")
try:
  f_hand = open(file_name)
except:
  print("File cannot be opened:", file_name)
  exit()

count = 0
for line in f_hand:
  words = line.split()
  if len(words) < 3 or words[0] != "From": continue
  count += 1
  print(words[1])

print(f"There were {count} lines in the file with From as the first word.")