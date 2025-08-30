class Parent:
    lname = "patil"
    def Info(self):
        print("Hello from parent ")
class Child(Parent):
    fname = "shubham"
    def education(self):
        print(" Education : BCA Graduate")

parent = Parent()
parent.Info()
# parent.education()

child = Child()
child.Info()
child.education()
    