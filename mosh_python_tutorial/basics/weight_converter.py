weight = input("Weight: ")
units = input("(L)bs or (K)g: ")

if units.lower() == 'l':
  print(f"You are {float(weight) / 2.205} kilos")
else:
  print(f"You are {float(weight) * 2.205} pounds")