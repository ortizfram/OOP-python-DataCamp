"""
Inheritance and polymorphism are the core concepts of OOP that enable efficient and consistent
code reuse. Learn how to inherit from a class, customize and redefine methods, and review the 
differences between class-level data and instance-level data.

  - Inheritance: extending functionality of existing code
  - Polymorphism : creating unified interface 
  - Encapsulation:  bundiling of data and methods
  
Why use class attributes? (global constants related to class ->)
  - min / max values for attributes
  - conmmonly used values / constants : e.g. pi for a circle class 
Class methods ?
  - already shared. Same code for every instance
  - can't use instance-level data
************************************************************************************"""
# Create a Player class
class Player: 
    
    # Class Attributes 
    MAX_POSITION = 10 
    
    # constructor
    def __init__(self):
        self.position = 0
""""""
# Print Player.MAX_POSITION       
print(Player.MAX_POSITION)

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.MAX_POSITION)
#------------------------------------------------------------------------#
class Player:
  # class attribute
    MAX_POSITION = 10
    
    #constructor
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        
        if(self.position + steps < Player.MAX_POSITION):
            self.position += steps
        else: 
            self.position = Player.MAX_POSITION
    

       
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
"""
<script.py> output:
    |----------
    ----|------
    ---------|-
    ----------|
 """
#------------------------------------------------------------------------#
# Create Players p1 and p2
p1 = Player()
p2 = Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# Assign 7 to p1.MAX_SPEED
p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)
#------------------------------------------------------------------------#
# Create Players p1 and p2
#change class attribute Player.MAX_SPEED
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE--- 
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)
#------------------------------------------------------------------------#
class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return BetterDate(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)
#------------------------------------------------------------------------#
""" map()  returns a map object(which is an iterator) of the results after applying the given function """
#---------------------------------------------------#
# import datetime from datetime
from datetime import datetime

class BetterDate:
    #contructor
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day

    #class method from_str
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, datetime):
        return BetterDate(datetime.year, datetime.month, datetime.day)

# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)
#------------------------------------------------------------------------#
""" inheritance : new class with all functionallity of old class + extra
e.g.  class Mychild(MyParent):
          # Do stuff   """
#------------------------------------------------------------------------#
# Create a subclass manager from employee class
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  pass

# Define a Manager object
mng = Manager('Debbie Lashko', 86500)

# Print mng's name
print(mng.name)
print(mng.salary)
#------------------------------------------------------------------------#
#custom child class
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
  # Add a constructor 
    def __init__(self, name, salary=50000, project= None):

        # Call the parent's constructor   
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project

  
    def display(self):
        print("Manager ", self.name)
