# try:
#     a = int(input('Enter a number '))
# except Exception as e:
#     print(e)
# print("thanks")


try:
    # typeError 
    a = int(input('Enter a number '))
    
    
    # Zero Division  
    sum = a / 0
except ZeroDivisionError as v:
    print(v)
except TypeError as e:
    print(e)    

print("thanks")