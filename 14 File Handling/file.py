'''

'''
# read file 
data = open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\file.txt")
reads = data.read()
print(reads)
data.close()



# write file
st = '''hey hello harry  
   content : Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:
“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”
The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.'''
f= open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\file.txt","w")
# f.write(st)
f.close()



# read one line 
f= open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\myfile.txt")
line1 = f.readline()
# print(line1,type(line1))

line2 = f.readline()
# print(line2,type(line2))

line3 = f.readline()
# print(line3,type(line3))

line4 = f.readline()
# print(line4,type(line4))
f.close()


# read multiple  line 
f= open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\myfile.txt")
lines = f.readlines()
# print(lines,type(lines))
f.close()


# append file
st = '''hey hello harry '''
f= open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\file.txt","a")
# f.write(st)
f.close()

# read file with binary  
data = open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\file.txt","rb")
reads = data.read()
# print(reads)
data.close()

# read file with binary  
data = open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\file.txt","rt")
reads = data.read()
# print(reads)
data.close()


# with statement same as a close() to close resource . dont need close() file 
with open("D:\\PythonDailyCode\\pythonwithVScode\\14 File Handling\\file.txt","rt") as f :
    f.read()










