import sys
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addnode(self,node):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node







if __name__ == '__main__':
    object = LinkedList() # linked list object created 
    #menu driven options 

    while True :
        print("1.Add node Linkedlist :")
        print('2.Add node in beginning :')
        print("3.Add node in between:")
        print("4.Add node in end :")
        print('5.Display linkedlist:')
        print("6.Exit:")

        ch = int(input("enter your choice:"))
        if ch == 1:
            value = int(input("Enter the value:"))
            object.addnode(value)
            print("node added successfully:")        