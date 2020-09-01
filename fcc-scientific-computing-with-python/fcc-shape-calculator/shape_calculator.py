class Rectangle:
  # Initializes a Rectangle instance
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  # Sets the width
  def set_width(self, width):
    self.width = width
  
  # Sets the height
  def set_height(self, height):
    self.height = height
  
  # Returns the are of the Rectangle instance
  def get_area(self):
    return self.width * self.height
  
  # Returns the perimeter of the Rectangle instance
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  # Returns the diagonal of the Rectangle
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  # Returns a string that represents the shape using lines of *
  def get_picture(self):
    if self.width > 50 or self.height > 50: return "Too big for picture."
    shape = ""
    for i in range(self.height):
      shape += "*" * self.width + "\n"
    return shape
  
  # Returns the number of times the passed in shape could fit inside this 
  # shape (with no rotations)
  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)
  
  # Returns a string representation of the Rectangle
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
  # Initializes a Square instance
  def __init__(self, side):
    self.width = self.height = side
  
  # Sets the side of the Square
  def set_side(self, side):
    self.width = self.height = side
  
  # Sets the width of the Rectangle
  def set_width(self, side):
    self.width = self.height = side
  
  # Sets the height of the Rectangle
  def set_height(self, side):
    self.width = self.height = side
  
  # Returns a string representation of the Square
  def __str__(self):
    return f"Square(side={self.width})"
