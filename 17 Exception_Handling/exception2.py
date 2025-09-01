#  raise exception
a= int(input("enter a Number 1:"))
b= int(input("enter a Number 2:"))
if(b==0):
    raise ZeroDivisionError("Number is not valid ")
else:
    print({a/b})

