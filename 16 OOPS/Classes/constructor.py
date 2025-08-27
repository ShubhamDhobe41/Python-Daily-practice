
class Employee:
    # class attribute
  language = "marathi"
  salary = 145678
     
  
  def __init__(self,language,salary):# dunder method call automatically 
    print("contructor called ........")
    self.language=language
    self.salary=salary   
      
shubham2 = Employee("eng",345678)
print(shubham2.salary,shubham2.language)










    