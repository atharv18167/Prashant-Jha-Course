

# class Base: #parent class
#     def __init__(self):
#         print("parent class constructor called")
#         self.a = "prashant" #public data variable
#         self.__c = "Ashish" #private member

# #creating a derived class / child class 
# class Derived(Base):
#     def __init__(self) :
#         #calling constructor of base class 
#         Base.__init__(self)
#         # print("calling private member of base class :")
#         # print(self.a)
#         # # print(self.__c)

# # obj1 = Derived()
# # print(obj1.a)
# # print(obj1.__c)


# obj2 = Base()
# print(obj2.a) #accesible cause it is public 
# print(obj2.__c) #not accessible cause it is private 



class Rbi :
    #declaring public method
    def publicPolicy(self):
        print("Check the public policy of Rbi")

    #declaring private method 
    def __privatePolicy(Self):
        print("There is some private policy which is not accesible for public")

class Sbi(Rbi):
    def __init__(self): #first sbi class const called 
        Rbi.__init__(self)  #second parent class constr called 
    
    def callingPublicMethod(self): #child class public method
        print("\nInside child class") 
        self.__publicPolicy() #calling parent class publi method

    def callingPrivateMethod(self): #child class public method 
        self.__privatePolicy()  #calling parent class private method

# obj1= Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()
obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__Rbi__privatePolicy()

    
