import random
'''
1 for snake 
-1 for water 
0 for gun 
'''
random_choice = random.choice([1,-1,0])
computer = random_choice
user = input('enter your choice : ')
youDict = {"s":1,"w":-1,"g":0}
you = youDict[user]
reverseDict={1:"snake", -1:"water", 0:"gun"}
print(f" You Choose {reverseDict[you]}\n Computer Choose {reverseDict[computer]}")
if(computer == you):
    print("its draw")
else:
    if(computer == -1 and you ==1 ):
        print("you win")
    elif(computer==-1 and  you ==0):
        print("you Lose")
    elif(computer==1 and  you ==-1):
        print("you Lose")
    elif(computer==1 and  you ==0):
        print("you win")
    elif(computer==0 and  you ==-1):
        print("you win")
    elif(computer==0 and  you ==1):
        print("you lose")
    else :
        print('wrong input ')
        


