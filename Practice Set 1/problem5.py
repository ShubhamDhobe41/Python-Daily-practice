# lebel the program in problem 4 with the comment
# import os
import os
# path of the directory you want to list
path = 'D:\PythonDailyCode\pythonwithVScode'  # Use '.' for the current directory, or specify another path
# list the content of the directory
content = os.listdir(path)
# print each item in the directory
for item in content:
    print(item)