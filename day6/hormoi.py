# 1.we can move only one disk at a time 
# 2 we have to pick upper disk d=from any one peice 
# 3 we have to place on top of any disk 
# 4 we cannot place any large disk on top of small disk
#tower of hanoi

import sys 
class Tower:
    def __init__(self):
        print("Tower of Hanoi")
        print()
        print("given problem   A=[3,2,1], B = [], C = []")
        print()
        print("expected output A =[], B =[] , C =[3,2,1]")
        self.A = []
        self.B = []
        self.C = []
        self.D = []

    def tower(self,item):
        self.A.append(item)
        print("A = ",self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2) #a=[3,2]
        self.C.append(self.temp) #c = [1] =>temp
        print("A =",self.A  , "B =",self.B , "C =",self.C)
        print("pass one completed================\n")

    def pass2(self):
        self.temp = self.A.pop(1) #a=[3,2]
        self.B.append(self.temp) #B = [2] =>temp
        print("A =",self.A  , "B =",self.B , "C =",self.C)
        print("pass two completed================\n")

    def pass3(self):
        self.temp = self.A.pop(0) #a=[3,2]
        self.B.append(self.temp) #C = [1] =>temp
        print("A =",self.A  , "B =",self.B , "C =",self.C)
        print("pass three completed================\n")

    def pass4(self):
        self.temp = self.A.pop(0) #a=[3,2]
        self.C.append(self.temp) #c = [1] =>temp
        print("A =",self.A  , "B =",self.B , "C =",self.C)
        print("pass four completed================\n")
    
    def pass5(self):
        self.temp = self.B.pop(0) #a=[3,2]
        self.C.append(self.temp) #c = [1] =>temp
        print("A =",self.A  , "B =",self.B , "C =",self.C)
        print("pass five completed================\n")
    def pass6(self):
        self.temp = self.B.pop(0) #a=[3,2]
        self.A.append(self.temp) #c = [1] =>temp
        print("A =",self.A  , "B =",self.B , "C =",self.C)
        print("pass six completed================\n")

obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj



        # print(self.A)
        # print(self.B)
        # print(self.C)
        # print(self.D)