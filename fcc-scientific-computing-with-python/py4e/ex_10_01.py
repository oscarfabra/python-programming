# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the 
# list in reverse order and print out the person who has the most commits.
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

tuples = []
for email, count in counts.items():
  tuples.append((count, email))

tuples.sort()
max_tuple = tuples[-1]
print(max_tuple[1], max_tuple[0])