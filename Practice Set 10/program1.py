# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer :
    company = "microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        
obj = Programmer("amol",1234567,413456)
print(obj.name,obj.salary,obj.pincode,obj.company)

obj1 = Programmer("ajay",8234567,487656)
print(obj1.name,obj1.salary,obj1.pincode,obj1.company)
        