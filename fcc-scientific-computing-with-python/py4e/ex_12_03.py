import urllib.request

url = input("Enter a URL: ")

try:
  fhand = urllib.request.urlopen(url)
except:
  print("URL could not be opened:", url)
  exit()

count = 0
for line in fhand:
  str = line.decode().strip()
  count += len(str)
  if count < 3000: print(str)

print("\nTotal number of characters:", count)