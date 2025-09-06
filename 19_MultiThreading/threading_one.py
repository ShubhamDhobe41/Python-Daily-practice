import threading
import time 

lock = threading.Lock()
print("Starting ")

def print_cube(num):
    with lock:
     print(f"Cube :{num * num * num}")
def print_square(num):
    with lock:
     print(f"Square :{num * num }")
    
if __name__=="__main__":
    t1=threading.Thread(target=print_cube,args=(10,))
    t2=threading.Thread(target=print_square,args=(4,))
    # start thread
    t1.start()
    t2.start()
    
    # join thread 
    t1.join()
    t2.join()
    
    print("Complete")
    