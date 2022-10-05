"""
In [1]:
type(mystery)
Out[1]:
__main__.Employee 
"""
#---------------------------------------------------#
""" type() to find the class attribute 
    dir()  to list all attributes and methods
    help() """
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
