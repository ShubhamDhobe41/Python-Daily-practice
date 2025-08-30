class Parent:
    fname = "manish"
    def Info(self):
        print("Hello from parent ")
class Child(Parent):
    fname = "ajay"
    def education(self):
        print(" Education : BCA Graduate")
class GrandSon(Child):
    fname="raj"
grandson = GrandSon()
print(grandson.fname)
grandson.Info()
grandson.education()