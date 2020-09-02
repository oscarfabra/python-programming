import copy
import random
# Consider using the modules imported above.

class Hat:
  # Initializes a new Hat instance
  def __init__(self, **balls):
    self.contents = []
    for color, count in balls.items():
      for i in range(count): self.contents.append(color)
  
  # Draws the specified number of balls from the hat
  def draw(self, num):
    if num > len(self.contents): num = len(self.contents)
    choices = []
    for i in range(num):
      ball = random.choice(self.contents)
      self.contents.remove(ball)
      choices.append(ball)
    return choices


# Tells whether the drawn_balls contain the expected_balls
def got_expected_balls(expected_balls, drawn_balls):
  for color, count in expected_balls.items():
    if drawn_balls.count(color) < count: return False
  return True


# Returns an estimated probability of getting at least the expected_balls with
# num_balls_drawn tries given the specified Hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    if got_expected_balls(expected_balls, drawn_balls): m += 1
  return m / num_experiments