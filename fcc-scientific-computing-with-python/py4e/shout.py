# Reads thorugh a file and prints the contents of the file (line by line)
# all in upper case
file_name = input("Enter a file name: ")
try:
  f_hand = open(file_name)
except:
  print("File cannot be opened:", file_name)
  exit()
for line in f_hand:
  line = line.rstrip().upper()
  print(line)
