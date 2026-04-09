#stack implemetation with size limit

import sys 
class Stack :
    def __init__(self,stacksize):
        self.stacklist = []  #stack created
        self.stacksize = stacksize 
    
    def isFull(self):
        if len(self.stacklist) == self.stacksize:
            return True
        else :
            return False
    def push(self,value):
        if self.isFull():
            print("stack is full")
        else : 
            self.stacklist.append(value)

    
    3.
    
    def displayStack(self):
        print("----------------------")
        print(self.stacklist)
        print("----------------------")

    
    def isEmpty(self):
        if self.stacklist == []:
            return True 
        else :
            return False

    def pop(self):
        if self.isEmpty():
           return "stack is empty"
        else :
            return self.stacklist.pop()
        
    def deleteStack(self):
        self.stacklist = None
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else :
            return self.stacklist[-1]

size = int(input("Enter the size of stack:"))     
stackObj = Stack(size)

while True :
    print("1.push element in stack:")
    print("2.Display stack element :")
    print("3.check Is Empty")
    print("4.Pop element from stack:")
    print("5.Delete stack:")
    print("6: Pick element from stack:")
    print("7.Exit:")

    choice = int(input("Enter your Choice:"))


    if choice == 1:
        val = int(input("Enter the value:"))
        stackObj.push(val)

    elif choice == 2:
        stackObj.displayStack()

    elif choice == 3:
        print(stackObj.isEmpty())

    elif choice == 4:
        print(stackObj.pop())

    elif choice == 5 :
        print(stackObj.deleteStack())

    elif choice == 6:
        print(stackObj.peek())

    elif choice == 7 :
        sys.exit()

