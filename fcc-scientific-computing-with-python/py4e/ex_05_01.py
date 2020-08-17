total = 0
count = 0
while True:
  num_str = input("Enter a number: ")
  if num_str == "done": break
  num = 0
  try:
    num = int(num_str)
  except:
    print("Invalid input")
    continue
  total += num
  count += 1
print(total, count, total / count if count != 0 else 0)