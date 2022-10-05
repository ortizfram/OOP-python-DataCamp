"""
In [1]:
type(mystery)
Out[1]:
__main__.Employee 
"""
#---------------------------------------------------#
""" type() to find the class attribute 
    dir(x) list all attributes and methods
    help(x) show the documentation for the object """
#---------------------------------------------------#
#Exploring object interface
# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)
#---------------------------------------------------#
""" help() or help(x) will show the documentation for the object or class x"""
#---------------------------------------------------#
#Exploring object interface

# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
#help(mystery) in console
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)
#---------------------------------------------------#
# Understanding class definition
Class My_Counter:
    
  def set_count(self, n):
    self.count = n
    
mc = My_Counter()
mc.set_count(5)
mc.count += 1
print(mc.count)
#---------------------------------------------------#
#Create your first class
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self, new_salary):
    self.salary = new_salary
  
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

