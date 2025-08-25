#  recursive function to calculate sum of first n natural numbers 
'''
sum(1)= 1
sum(2)= 1 + 2
sum(3)= 1 + 2 + 3 
sum(4)= 1 + 2 + 3 + 4 
sum(5)= 1 + 2 + 3 + 4 + 5
 sum(n)= 1 + 2 + 3 + 4 +.....n
'''

def sumNaturalNo(n):
    if(n==1):
        return 1
    return sumNaturalNo(n - 1) + n 

# print(sumNaturalNo(4))

n = int(input('Enter a Number : '))
res = sumNaturalNo(n)
print(res)