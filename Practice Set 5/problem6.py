#  create dictionary . allow 4 friend to enter language as a value and name as a key assume name are unique 
dict1 = {}

for i in range(4):
    name = input('Enter Name : ')
    lang = input('Enter language : ')
    dict1.update({name:lang})
print(dict1)
    