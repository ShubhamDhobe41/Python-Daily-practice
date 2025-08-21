#  find a student has passed or failed if it require a total 40 and least 33 in each subject to pas asume 3 subject and take marks as an input from user 
marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))  
marks3 = int(input("Enter marks for Subject 3: "))
total_marks =(100 * (marks1 + marks2 + marks3))/300
if total_marks >= 0.40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("Student has passed." + str(total_marks * 100) + "%")
else:
    print("Student has failed.")    




