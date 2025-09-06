import threading

lock = threading.Lock()

def task(name):
    print(f"{name} trying to acquire lock...")
    lock.acquire()   # take the lock
    print(f"{name} acquired the lock!")
    for i in range(3):
        print(f"{name} working {i+1}")
    lock.release()   # give back the lock
    print(f"{name} released the lock.")

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()
t1.join()
t2.join()
