#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # file = open("textfile.txt", "w+")

  # Open the file for appending text to the end
  file = open("textfile.txt", "r")

  # write some lines of data to the file
  # for i in range(10):
  #   file.write("This is line " + str(i + 1) + "\n")
  
  # close the file when done
  # file.close()
  
  # Open the file back up and read the contents
  if file.mode == 'r':
    # contents = file.read()
    # print(contents)
    file_lines = file.readlines()
    for line in file_lines:
      print(line, end = '')
    
if __name__ == "__main__":
  main()
