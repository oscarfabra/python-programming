# Figure out who has the most messages in the file. After all the data has been
# read and the dictionary has been created, look through the dictionary using a 
# maximum loop to find who has the most messages and print how many messages 
# the person has.
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

max_count = None
max_email = None
for email, count in counts.items():
  if max_count is None or count > max_count:
    max_count = count
    max_email = email

print(max_email, max_count)