'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways
'''
import random
class Train :
    
    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def bookTicket(self,fromDist,to):
        print(f"Ticket is Book in train No :{self.trainNo} from {fromDist} to {to}")
        
    def getStatus(self):
        print(f"Tarin No {self.trainNo} is running on time ")
        
    def getFare(self,fromDist,to):
                print(f"Ticket is Fare in train No :{self.trainNo} from {fromDist} to {to} is {random.randint(222,554)}")
        
obj = Train(1234)
obj.bookTicket("pune","mumbai")
obj.getStatus()
obj.getFare("lakhnow","delhi")