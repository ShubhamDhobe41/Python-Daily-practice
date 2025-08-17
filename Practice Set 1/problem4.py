# write a program to print the content of a directory using the os module search online for the function which does that 
import os

path = 'D:\PythonDailyCode\pythonwithVScode'  # Use '.' for the current directory, or specify another path
content = os.listdir(path)
for item in content:
    print(item)