import threading
import time
lock = threading.Lock()

def print_num_asc():
    with lock:
        for i in range(1,11):
            print(i)
            time.sleep(0.5)
            
def print_num_dec():
    with lock:
        for i in range(10,0,-1):
            print(i)
            time.sleep(0.5)
            
t1= threading.Thread(target=print_num_asc)
t2= threading.Thread(target=print_num_dec)

t1.start()
t2.start()

t1.join()
t2.join()

print("complete")
  