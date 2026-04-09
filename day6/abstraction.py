# from abc import ABC, abstractmethod # abstractmethod
# class Help4code(ABC): # abstract class
#     @abstractmethod #decorator
#     def training(self): # abstract method
#         pass
#     def placement(self): #abstract method
#         pass

# class Ashish (Help4code):
#     def training(self):
#         print('c','C++','Java')
#     def placement(self):
#         print("java Placement")

# class Ankush(Help4code):
#     def training(self):
#         print('python','Django')
#     def placement(self):
#         print("Python Placement")

# obj1 = Ashish()
# obj1.training()
# obj1.placement()

# obj2= Ankush()
# obj2.training()
# obj2.placement()





from abc import ABC,abstractmethod 
class Irctc (ABC):
    @abstractmethod 
    def bookTicket(self): #abstractmethod
        pass

class MakeMyTrip(Irctc):
    def bookTicket(self):
        print("   =======================================================")
        print("   Welcome to makemytrip.com    ")
        source      = input("Enter a source station name:")
        destination = input("Enter a destination name:")
        date        = input ("Enter a date:")
        print("===========================================================")

class GoIbibo(Irctc):
    def bookTicket(self):
        print("   Welcome To yatra.com")
        source      =  input("Enter a source station name:")
        destination = input("Enter a destination name:")
        date        = input ("Enter a date:")
    
obj1 = MakeMyTrip()
obj1.bookTicket()

obj2=GoIbibo()
obj2.bookTicket()