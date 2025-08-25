# find greatest of three number using function 
def grethestNumber(a,b,c):
    if(a > b and a > c):
        print("a is greater")
    elif(b > a and b > c):
        print("b is greater")
    else:
        print(" c is greater")

grethestNumber(22,44,53)