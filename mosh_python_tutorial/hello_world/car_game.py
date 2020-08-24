cmd = ""
moving = False

while True:
  cmd = input("> ").lower()
  if cmd == "help":
    print('''
start - to start the car
stop - to stop the car
quit - to exit
    ''')
  elif cmd == "start":
    if not moving:
      print("Car started... ready to go!")
      moving = True
    else:
      print("You already started!")
  elif cmd == "stop":
    if moving:
      print("Car stopped.")
      moving = False
    else:
      print("You haven't started!")
  elif cmd == "quit":
    break
  else:
    print("I don't understand that...")