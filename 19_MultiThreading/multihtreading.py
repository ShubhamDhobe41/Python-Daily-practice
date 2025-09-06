import threading
import time 

# def func(seconds):
#     print(f"Sleeping for {seconds} seconds ")
#     time.sleep(seconds)
# Normal Code 
# time1=time.perf_counter()
#  print(time1)
# func(4)
# func(9)
# func(2)
# time2=time.perf_counter()
# print(time2-time1)


# code using MultiThreading
# time1=time.perf_counter()
# t1=threading.Thread(target=func,args=[5])
# t2=threading.Thread(target=func,args=[3])
# t3=threading.Thread(target=func,args=[7])
# t1.start()
# t2.start()
# t3.start()

# if you want to wait for t1,t2 and t3 
# t1.join()
# t2.join()
# t3.join()

# calculate time 
# time2=time.perf_counter()
# print(time1 - time2)
    

# Without Threading
# import time
# def task(name):
#     print(f"Starting {name}")
#     time.sleep(2)
#     print(f"Finished {name}")
# # Run tasks one by one
# task("Task 1")
# task("Task 2")

# with Multithreading
import threading
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

# Create threads
t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))
# Start threads
t1.start()
t2.start()
# Wait for both to finish
t1.join()
t2.join()
print("All tasks done!")


 