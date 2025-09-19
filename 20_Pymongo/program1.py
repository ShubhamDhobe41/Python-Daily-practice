# Write a mangodb program to create a books collection having field Title, Author, Publisher, Price. Write a code to perform following operations. First one is insert 5 documents into books collection. Second one is retrieve books which published is a person. Third one is retrieve books whose price is between 400 to 600. Fourth one is retrieve books in the descending order of price. Fifth one is update the price of the book by 10% whose title is a python. Sixth one is update the title of the book whose author is a Guido and publisher is a bpb.

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db=client['mydb']
books_collection= db['Books']

books = [
    {"Title": "Python Basics", "Author": "Guido", "Publisher": "BPB", "Price": 500},
    {"Title": "Learning Java", "Author": "James Gosling", "Publisher": "Pearson", "Price": 450},
    {"Title": "MongoDB Guide", "Author": "Dwight", "Publisher": "O'Reilly", "Price": 600},
    {"Title": "C Programming", "Author": "Dennis Ritchie", "Publisher": "McGraw Hill", "Price": 350},
    {"Title": "JavaScript Essentials", "Author": "Brendan Eich", "Publisher": "Pearson", "Price": 550},
]

books_collection.insert_many(books)
print("insert Successfully")

# retrive books whose publisher is person 

for book in  books_collection.find({"Publisher": "Person"}):
    print(book)
