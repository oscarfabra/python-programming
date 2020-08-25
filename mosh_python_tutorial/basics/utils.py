# Returns the largest number in the given list
def find_max(numbers):
  largest = None
  for num in numbers:
    if largest is None or num > largest: largest = num
  return largest