class MyException(Exception):
    pass

def do_action(x):
       if x < 0 :
        raise MyException("Negative value not allowed!") 
try:
    do_action(-3)
except MyException as e :
    print("Caught custom exception:", e)
     
     
     
    