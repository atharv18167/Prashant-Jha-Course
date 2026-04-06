# # # it has the ability of a message to be displayed in more than one form 
# # # polymorphism example 
# # class Principal :
# #     def role(self):
# #         print("i am managing all acitivies of the college") #polymorphism is the ability of the college

# # class Dean :
# #     def role(self):
# #         print('Dean = I am decison taking person')

# # class Hod :
# #     def role (self):
# #         print('Hod = i have responsibities of teachers and students')

# # class Faculty :
# #     def role(self):
# #         print('I am a teacher')

# # def func(obj): #calling func obj =1 :Dean
# #     obj.role() #calling func
# # campus =[Principal(),Dean(),Hod(),Faculty()]
# # for obj in campus: #obj =[0:principal,1:Dean,2:Hod,3:Faculty]
# #     func(obj) #func calling 




# # # overloading : python does not support method overloading 
# class Arithmetic :
#     def add (self,a):
#         print(a)

#     def add (self,a,b):
#         print(a+b)
#     def add (self,a,b,c) :
#         print(a+b+c)
# obj = Arithmetic()
# # obj.add(10)
# # obj.add(10,20)
# obj.add(1,2,3)
        

# class Arithmetic :
#     def add (self,a=None,b=None,c=None):
#         if a!=None and b!=None :
#             print(a+b)
#         elif a!=None and b!=None and c!=None :
#             print(a+b+c)
#         else :
#             print("enter atleast two argument")
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

# class Arithmetic :
#     def __init__(self):
#         print("there is no argument")
#     def __init__(self,a):
#         print("passing one argument")
#     def __init__(self,a,b):
#         print("passing two argument")

# # obj = Arithmetic()
# # obj = Arithmetic(10)
# obj = Arithmetic(2,2)






#overriding (parent and child realtionship must be there )
# class Rbi :
#     def home_loan(self):
#         print("home loan = 7.5")
#     def car_loan(self):
#         print("car loan = 8.5")

# class Sbi (Rbi):
#     def home_loan(self):
#         print("sbi provide home loan = 8.9")
#         super().home_loan() #we can acces parent class method in child in class using super method 
#     def car_loan(self):
#         print("sbi provide car loan = 9.9")
       

# obj = Sbi()
# obj.home_loan()
# obj.car_loan()





#constructor overriding 
class Father :
    def __init__(self):
        print("Father: i am already at breakfast table:")

class Son (Father):
    def __init__(self):
        print("Son: i will be late for breakfast:")
        # super().__init__()

obj= Son ()