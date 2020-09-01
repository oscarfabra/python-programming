class Category:
  # Initializes a new Category instance
  def __init__(self, name):
    self.name = name
    self.ledger = []

  # Appends a dictionary with the deposit to the ledger list
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  # Returns True if the withdrawal took place, False otherwise
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  # Returns the current balance based on the transactions that have taken place
  def get_balance(self):
    total = 0
    for transaction in self.ledger:
      total += transaction["amount"]
    return total
  
  # Transfers the given amount to the given Category object
  def transfer(self, amount, other_category):
    if self.withdraw(amount, "Transfer to " + other_category.name):
      other_category.deposit(amount, "Transfer from " + self.name)
      return True
    return False
  
  # Returns True if the current balance is greater than or equal to the amount
  def check_funds(self, amount):
    return self.get_balance() >= amount
  
  # Returns a String representation of the current Category instance
  def __str__(self):
    output = ""
    output += self.name.center(30, '*') + '\n'
    total = 0
    for transaction in self.ledger:
      output += transaction["description"].ljust(23)[:23]
      output += "{:.2f}".format(transaction["amount"]).rjust(7)[:7] + "\n"
      total += transaction["amount"]
    output += "Total: " + str(total)
    return output


# Gets the total spend of the given category
def get_category_spend(category):
  spend = 0
  for transaction in category.ledger:
    if transaction["amount"] < 0: spend += transaction["amount"]
  return round(-spend, 2)


# Returns a dictionary with the rounded percentages for each category
def get_percentage_spent_by_category(categories):
  categories_spend = {}
  total_spend = 0
  for category in categories:
    category_spend = get_category_spend(category)
    categories_spend[category.name] = category_spend
    total_spend += category_spend
  percentages = {}
  for name, spend in categories_spend.items():
    percentages[name] = (spend * 100 / total_spend) // 10 * 10
  return percentages


# Returns the string with the bar chart
def build_chart_str(percentages):
  output = ""
  for label in range(100, -1, -10):
    output += f"{label}|".rjust(4) + " "
    for percentage in percentages:
      output += "o  " if percentage >= label else "   "
    output += '\n'
  output += (" " * 4) + "-" * (len(percentages) * 3 + 1) + "\n"
  return output


# Returns the length of the longest category name
def calc_depth_of_names(names):
  longest = 0
  for name in names:
    if len(name) > longest: longest = len(name)
  return longest


# Returns the string with the category names displayed vertically
def build_names_str(names):
  output = ""
  depth = calc_depth_of_names(names)
  for i in range(depth):
    output += " " * 5
    for name in names:
      output += name[i] + "  " if i < len(name) else "   "
    output += "\n"
  return output


# Creates a bar chart based on the given categories' withdrawals
def create_spend_chart(categories):
  output = "Percentage spent by category\n"
  percentages = get_percentage_spent_by_category(categories)
  output += build_chart_str(percentages.values())
  output += build_names_str(percentages.keys())
  return output[:-1]