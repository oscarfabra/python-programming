class Person:
  def __init__(self, name):
    self.name = name
  
  def talk(self):
    print(f"{self.name} is talking...")


person_1 = Person("Oscar")
person_1.talk()