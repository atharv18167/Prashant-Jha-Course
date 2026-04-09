#stack implemetation with size limit

import sys 
class Queue :
    def __init__(self,queuesize):
        self.queuelist = []  #stack created
        self.queuesize = queuesize 
    
    def isFull(self):
        if len(self.queuelist) == self.queuesize:
            return True
        else :
            return False
    def Enqueue(self,value):
        if self.isFull():
            print("Queue is full")
        else : 
            self.queuelist.append(value)

    
    def displayQueue(self):
        print("----------------------")
        print(self.queuelist)
        print("----------------------")

    
    def isEmpty(self):
        if self.queuelist == []:
            return True 
        else :
            return False

    def Dequeue(self):
        if self.isEmpty():
           return "Queue is empty"
        else :
            return self.queuelist.pop(0)
        
    def deleteQueue(self): #delete dequeue
        self.queuelist = []
        return "Queue is Deleted"
    
    def peek(self): # returns first element of queue 
        if self.isEmpty():
            return "queue is empty"
        else :
            return self.queuelist[0] #slicing of list 

size = int(input("Enter the size of Queue:"))     
queueObj = Queue(size)

while True :
    print("1.Enqueue element in Queue:")
    print("2.Display Queue element :")
    print("3.check Is Empty")
    print("4.Dequeue element from Queue:")
    print("5.Delete Queue:")
    print("6: Pick element from Queue:")
    print("7.Exit:")

    choice = int(input("Enter your Choice:"))


    if choice == 1:
        val = int(input("Enter the value:"))
        queueObj.Enqueue(val)

    elif choice == 2:
        queueObj.displayQueue()

    elif choice == 3:
        print(queueObj.isEmpty())

    elif choice == 4:
        print(queueObj.Dequeue())

    elif choice == 5 :
        print(queueObj.deleteQueue())

    elif choice == 6:
        print(queueObj.peek())

    elif choice == 7 :
        sys.exit()

