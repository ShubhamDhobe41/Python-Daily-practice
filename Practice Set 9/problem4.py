# Write a program to make a copy of a text file “this.txt"
with open("D:\\PythonDailyCode\\pythonwithVScode\\Practice Set 9\\this.txt", "r") as f:   # Open original file in read mode
    content = f.read()             # Read everything

with open("copy.txt", "w") as f:   # Open new file in write mode
    f.write(content) 
    print(f.write(content))