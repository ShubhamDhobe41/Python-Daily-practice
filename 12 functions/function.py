def greet():
    print("hello from function")
    
# greet()


def avarage():
    a=int(input('enter a number '))
    b=int(input('enter a number '))
    c=int(input('enter a number '))
    
    avg = (a+b+c)/3
    return avg
# res = avarage()
# print(res)

# arguments in python
def goodDay(name,greeting):
    print("Hello "+name)
    print(greeting)
    return "calling"
# a= goodDay("rahul","thank you")
# print(a)

# default argument
def Info(name,age=33):
    print(f"Name is ,{name} and age is ,{age}")
Info("rahul")
# Info("manish",23)



