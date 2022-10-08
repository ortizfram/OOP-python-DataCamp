"""
//// operator & method  ////         
      ==    __eq__()        2 objects of a class are compared using ==, (self and other), returns Boolean
      !=    __ne__()        
      >=    __ge__()
      <=    __le__()
      >     __gt__()
      <     __lt__() """
#----------------------------------------------------------------------------------#
class BankAccount:
   # MODIFY to initialize a number attribute
    def __init__(self,number,balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount 
    
    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
#----------------------------------------------------------------------------------#
#Checking class equality
class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number) and \
        (type (self) == type(other) )

acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)
#----------------------------------------------------------------------------------#
""" <- when comparing a child object to a parent object
    Python always calls the child's __eq__() method ."""
#----------------------------------------------------------------------------------#
#String formatting review
my_num = 5
my_str = "Hello"

#f = ...
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str) 
print(f)
# my_num is 5, and my_str is "Hello".
#----------------------------------------------------------------------------------#
""" <- you use \"  \"  to scape quotation mark function & just for them to appear as decoration ."""
#----------------------------------------------------------------------------------#
"""Add the __str__() method to Employee that satisfies the following:

      - If emp is an Employee object with name "Amar Howard" and salary of 40000, then print(emp) outputs"""
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__(self):
        output = """
        Employee name:{name}
        Employee salary:{salary}
        """.format(name = self.name, salary = self.salary)
        return output

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)
"""  output:
            Employee name:Amar Howard
            Employee salary:30000
            
            Employee name:Carolyn Ramirez
            Employee salary:35000"""
#----------------------------------------------------------------------------------#
#String representation of objects
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):
        
        return "Employee(\"{name}\", {salary})".format(name = self.name, salary = self.salary)


emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))
"""output:
Employee("Amar Howard", 30000)
Employee("Carolyn Ramirez", 35000)"""
