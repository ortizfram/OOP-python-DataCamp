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
