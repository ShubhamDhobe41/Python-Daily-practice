#  sum of first n natural number using while loop
n = int(input("Enter a number: "))
i = 1   
sum = 0
while(i<=n):    
    sum = sum + i
    i = i + 1 
print("The sum is",sum)