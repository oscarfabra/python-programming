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


def create_spend_chart(categories):
  output = ""
  # TODO: Build output
  return output