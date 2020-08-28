def arithmetic_arranger(problems, display_answers = False):
  arranged_problems = ""

  if len(problems) > 5: return "Error: Too many problems."
  if not has_correct_operators(problems): return "Error: Operator must be '+' or '-'." 
  if not operands_only_contain_digits(problems): return "Error: Numbers must only contain digits."
  if not operands_contain_max_four_digits(problems): return "Error: Numbers cannot be more than four digits."

  # TODO

  return arranged_problems


# Checks whether the given problems contain only addition or subtraction.
def has_correct_operators(problems):
  for problem in problems:
    operator = problem.split()[1]
    if operator != '+' and operator != '-': return False
  return True

# print(has_correct_operators(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(has_correct_operators(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))


# Checks whether the given numbers contain only digits
def operands_only_contain_digits(problems):
  for problem in problems:
    pieces = problem.split()
    if not pieces[0].isdigit() or not pieces[2].isdigit(): return False
  return True

# print(operands_only_contain_digits(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(operands_only_contain_digits(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))


# Checks whether the given numbers contain maximum 4 digits
def operands_contain_max_four_digits(problems):
  for problem in problems:
    pieces = problem.split()
    if len(pieces[0]) > 4 or len(pieces[2]) > 4: return False
  return True

# print(operands_contain_max_four_digits(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(operands_contain_max_four_digits(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))