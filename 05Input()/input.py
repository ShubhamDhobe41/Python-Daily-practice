# problem with the above code is that it takes input as string
a= input('Enter a number 1 : ')
b= input('Enter a number 2 : ')
print("Number is :",a)
print("Number is :",b)
# the output is string
print("Sum is :", a + b) 

print("Sum is :", int(a) + int(b)) 

# solution of the problem is that input is taken as string
a= int(input('Enter a number 1 : '))
b= int(input('Enter a number 2 : '))
print("Number is :",a)
print("Number is :",b)
# the output is string
print("Sum is :", a + b) 

print("Sum is :", int(a) + int(b)) 
