marks ={
    "rohan ": 98,
    "shubham": 95,  
    "priyanshu": 90,
    "priyanshu": 90, # Duplicate keys are not allowed, this will overwrite the previous value
    "sahil": 85,        
    "siddharth": 80,
    "list": [1, 2, 3, 4, 5],
}

# marks["rohan "] = 100
# print(marks)
# print(type(marks))

# print(marks["rohan "])
# print(marks["siddharth"]) 
# print(marks["list"])  


# Methods in dictionaries
# print(marks.keys())  # Returns a view object that displays a list of all the keys
# print(marks.values())  # Returns a view object that displays a list of all the values
# print(marks.items())  # Returns a view object that displays a list of dictionary's key-value tuple pairs

# print(marks.update({"rohan": 100}))  # Updates the value for the key "rohan" to 100
# print(marks)

# print(marks.get("shubham"))  # Returns the value for the key "shubham"
# print(marks["shubham"])

# print(marks.get("shubham1"))  # Returns the value for the key "shubham"
# print(marks["shubham1"]) # Raises KeyError since "shubham1" does not exist in the dictionary

# print(marks.pop("rohan "))  # Removes the key "rohan " and returns its value

# print(marks.popitem())  # Removes the last inserted key-value pair and returns it

# print(marks.clear())  # Removes all items from the dictionary

# print(len(marks))  # Returns the number of items in the dictionary