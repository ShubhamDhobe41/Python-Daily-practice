# Write a class “Calculator” capable of finding square, cube and square root of a number
class Calculator :
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The sqaure is : {self.n*self.n}")
    def cube(self):
        print(f"The cube is : {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The sqaure  root is : {self.n**1/2}")
    
a=Calculator(5)
a.square()
a.cube()
a.squareRoot()
        