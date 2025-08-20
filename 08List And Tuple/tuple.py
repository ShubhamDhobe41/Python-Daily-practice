# tuple are immutable and list are mutable
friends = ("apple", "orange", 5, 3772, False, "Akash")
print(friends)
# print(type(friends))


# friends[0]="mango"  # This will raise an error since tuples are immutable
# print(friends)


a=(1)
# print(type(a))  # This will print <class 'int'>, not a tuple
a=(1,)  
# print(type(a))  # This will print <class 'tuple'>, as it is a single-element tuple



# methods
a=(1, 2, 3, 4, 5,5,2,3,4,5,6,7,8,9)

no =  a.count
# print(no(2))  


# print(a.index(5)) 

# print(a.index(5, 5))  # This will find the index of the first occurrence of 5 after the 5th index

# print(len(a))  # This will print the length of the tuple

# print(a[1:5])  # This will slice the tuple from index 1 to 4 (5 is not included)

# print(a[1:5:2])  # This will slice the tuple from index 1 to 4 with a step of 2

# print(a[::-1])  # This will reverse the tuple

b,c,d =(1, 2, 3)  # Tuple unpacking
# print(b, c, d)  # This will print 1 2 3
# print(b);


