def convert_message(msg):
  words = msg.split()
  emojis = {
    ":)": "😀",
    ":(": "☹️"
  }
  str = ""
  for word in words:
    str += emojis.get(word, word) + " "
  return str


message = input("> ")
print(convert_message(message))