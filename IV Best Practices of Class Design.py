"""   - Polymorphism : using unified interface to operate on objects or different clases 
*****************************************************************************************************"""
# Polymorphic methods
# identify the output
class Parent:
    def talk(self):
        print("Parent talking!")     

class Child(Parent):
    def talk(self):
        print("Child talking!")          

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()
"""output : 
Parent talking!
Child talking!
Talkative Child talking!
Parent talking!"""
#-------------------------------------------------------------------------#
# 2.a
# Define a Rectangle class
class Rectangle():
    def __init__(self,h, w):
        self.h = h
        self.w= w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        Rectangle.__init__(self,w,w)
""" <- Square constructor that accepts one parameter w, and sets both
the h and w attributes to the value of w."""
#-------------------------------------------------------------------------#
# 2.b
