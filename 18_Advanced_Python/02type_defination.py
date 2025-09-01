'''
Type Hints (Type Definitions in Functions)
Since Python 3.5, you can use type hints to define what type of data a variable or function should use.
This is not enforced at runtime but helps readability and tools like IDEs and linters.
'''

n : int=33

name : str="welcome"

def sum(a:int,b:int)->int :
    sumTwo = a + b
    return sumTwo
# print(sum(12,32))
result : int = sum(23,43)
print(result)
