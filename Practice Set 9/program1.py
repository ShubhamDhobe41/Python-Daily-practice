'''
Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’.
'''

with open("D:\\PythonDailyCode\\pythonwithVScode\\Practice Set 9\\poems.txt","r") as data:
 reads= data.read().lower()
# read file 
if("twinkle".lower() in reads):
  print(f"Yes, the word  is present ")
else:
     print(f"No, the word  is not present")
data.close()

