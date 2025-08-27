'''
Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old.
'''

import os

def multi():
    # Create folder if it does not exist
    os.makedirs("Tables_for_13_year_old", exist_ok=True)

    # Generate tables
    for i in range(2, 21):
        with open(f"Tables_for_13_year_old/Table_of_{i}.txt", "w") as data:
            for j in range(1, 11):
                data.write(f"{i} x {j} = {i*j}\n")

multi()


