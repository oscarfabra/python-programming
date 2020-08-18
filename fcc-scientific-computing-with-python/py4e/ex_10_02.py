# This program counts the distribution of the hour of the day for each of the
# messages. You can pull the hour from the “From” line by finding the time 
# string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, 
# one per line, sorted by hour.

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
  hour = words[5].split(":")[0] 
  counts[hour] = counts.get(hour, 0) + 1

for hour, count in sorted(counts.items()):
  print(hour, count)
