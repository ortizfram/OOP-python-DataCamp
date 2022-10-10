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
""" <- in the console or the script pane, create a Square object with side length 4. Then try assigning 7 to the h attribute.
What went wrong with these classes

# option 3 :
The 4x4 Square object would no longer be a square if we assign 7 to h."""
#-------------------------------------------------------------------------#
# 2.c
class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h

# Define set_h to set h      
    def set_h(self, h):
      self.h = h
      
# Define set_w to set w          
    def set_w(self,w):
      self.w = w
      
#set both attributes to w      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 
e
# Define set_h to set w to h attribute
    def set_h(self, h):
      self.h = h
      self.w = h

# Define set_w to set h wo w attribute    
    def set_w(self,w):
      self.w= w
      self.h= w 
#-------------------------------------------------------------------------#
# 2.d
""" <- How does using these setter methods violate Liskov Substitution principle?
option 2 : 

Each of the setter methods of Square change both h and w attributes, while 
setter methods of Rectangle change only one attribute at a time, so the Square 
objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant."""
#-------------------------------------------------------------------------#
"""*************************************************************************
Restricting access methods: 
    - naming conventions: 
        - start with single '_' --> "internal" , not part of public API
        - start with couble '__' -> "private" (psudo attributes), to prevent name clashes in inherited classes
      >  Only used for built-in methods (__init__(), __repr__()) 
    - use @property to customize access:
    - Overriding __getattr__(), __Setattr__():
****************************************************************************"""
