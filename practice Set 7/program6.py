#  factorial of a number using for loop
num = int(input("Enter a number: "))

for i in range(1,num):
    num = num*i
print("The factorial is",num)