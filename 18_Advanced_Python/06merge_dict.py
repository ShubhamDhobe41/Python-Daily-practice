# merging and updating dictionaries 

dict1 ={"a":1,"b":2}
dict2 ={"c":3,"d":4}

merged = dict1 | dict2
print(merged)


with(
    open("D:\\PythonDailyCode\\pythonwithVScode\\18_Advanced_Python\\file1.txt","r") as f1,
    open("D:\\PythonDailyCode\\pythonwithVScode\\18_Advanced_Python\\file2.txt","w") as f2
):
   data = f1.read()
   print(f2.write(data))