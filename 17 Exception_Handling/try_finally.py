def main():
    try:
        a = int(input('Enter a number '))
        b = int(input('Enter a number '))
    # Zero Division  
        sum = a / b
        # return
    
    except ZeroDivisionError as v:
           print(v)
           return
    else:
         print("executed") 
    finally:
         print("finally Executed") 
main()
print("thanks")
