try:

    a = int(input('Enter a number '))
    b = int(input('Enter a number '))
  
    # Zero Division  
    sum = a / b
except ZeroDivisionError as v:
    print(v)
else:
    print("executed")  

print("thanks")