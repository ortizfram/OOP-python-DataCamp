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
    MAX_POSITION = 10
    
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
