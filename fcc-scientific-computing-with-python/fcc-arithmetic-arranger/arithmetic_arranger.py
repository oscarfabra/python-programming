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


# Builds the first line to display based on the given problems
def build_first_line(problems):
  first_line = ""
  for problem in problems:
    if first_line != "": first_line += " " * 4
    a, b = problem.split()[0], problem.split()[2]
    problem_length = max(len(a), len(b)) + 2
    first_line += " " * (problem_length - len(a))
    first_line += a
  return first_line

# print(build_first_line(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(build_first_line(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))


# Builds the second line to display based on the given problems
def build_second_line(problems):
  second_line = ""
  for problem in problems:
    if second_line != "": second_line += " " * 4
    a, op, b = problem.split()
    problem_length = max(len(a), len(b)) + 2
    second_line += op + " " * (problem_length - len(b) - 1)
    second_line += b
  return second_line

# print(build_second_line(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(build_second_line(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))


# Builds the dashes below the operands for the given problems
def build_dashes_line(problems):
  dashes_line = ""
  for problem in problems:
    if dashes_line != "": dashes_line += " " * 4
    a, b = problem.split()[0], problem.split()[2]
    problem_length = max(len(a), len(b)) + 2
    dashes_line += "-" * problem_length
  return dashes_line

# print(build_dashes_line(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(build_dashes_line(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))


# Builds the answers line for the given problems
def build_answers_line(problems):
  answers_line = ""
  for problem in problems:
    if answers_line != "": answers_line += " " * 4
    a, op, b = problem.split()
    problem_length = max(len(a), len(b)) + 2
    answer = int(a) + int(b) if op == "+" else int(a) - int(b)
    answer_length = len(str(answer))
    answers_line += " " * (problem_length - answer_length)
    answers_line += str(answer)
  return answers_line

# print(build_answers_line(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]))


# Returns the problems arranged vertically and side-by-side according to the rules given by README.md
def arithmetic_arranger(problems, display_answers = False):
  arranged_problems = ""

  if len(problems) > 5: return "Error: Too many problems."
  if not has_correct_operators(problems): return "Error: Operator must be '+' or '-'." 
  if not operands_only_contain_digits(problems): return "Error: Numbers must only contain digits."
  if not operands_contain_max_four_digits(problems): return "Error: Numbers cannot be more than four digits."

  arranged_problems += build_first_line(problems) + "\n"
  arranged_problems += build_second_line(problems) + "\n"
  arranged_problems += build_dashes_line(problems)
  if display_answers: arranged_problems += "\n" + build_answers_line(problems)

  return arranged_problems

# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))