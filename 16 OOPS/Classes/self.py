class Employee:
 # class attribute
  language = "marathi"
  salary = 145678
  
  def getInfo(self):
      print(f"The language is {self.language} the salary is {self.salary}")
    #   selef is important in method because is treted as 1 argument will passed  "Employee.greet(shubham)". 
  def greet(self):
      print("Good Morning ")
  
shubham = Employee()
shubham.getInfo()
shubham.greet()
# Employee.greet(shubham)







    