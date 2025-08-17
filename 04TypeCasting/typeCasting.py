# type() is used to check the type of a variable
a=23
b="Hello"
# print(type(a))
# print(type(b)) 

#  Type casting is used to convert one data type to another

a=34
a= str(a)  # Converting integer to string
print(type(a))  # Output: <class 'str'>

b=45.67
b= int(b)  # Converting float to integer        
print(type(b))  # Output: <class 'int'>

c="123"
c= float(c)  # Converting string to float       
print(type(c))  # Output: <class 'float'>

d=56
d= bool(d)  # Converting integer to boolean (non-zero integer is True)  
print(type(d))  # Output: <class 'bool'>

e="False"
e= bool(e)  # Converting string to boolean (non-empty string is True)   
print(type(e))  # Output: <class 'bool'>

