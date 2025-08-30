class Father:
    fname = "manish"
    def Info(self):
        print("Hello from parent ")
class Mother:
    fname = "ajay"
    def education(self):
        print(" Education : BCA Graduate")
class child(Father,Mother):
    fname="raj"
    def education(self):
        print(" Education :  Graduate")
child = child()
print(child.fname)
child.Info()
child.education()
