#object oriented programming

# class Student :

#     roll_no = 101 #data member

#     def studentData(self): #method/member function
#         print("Student Information")

# obj = Student()
# print(obj.roll_no)
# obj.studentData()



# class Demo :
#     def __init__(self) :
#         print("I am constructor")
    
#     def msg(self):
#         print("hello class !")

# obj1 = Demo()
# obj2 = Demo()
# obj1.msg()




# class Hod :
#     def __init__(self):
#         self.name = "prashant"
#         self.age = 20
#         self.empid = 1001
    
#     def info(self):
#         print("My name is:",self.name)
#         print("My age is:",self.age)
#         print("My empid is:",self.empid)
# obj = Hod()
# obj.info()/



# class Hod :
#     def __init__(self,name,age,rollno):
#         self.name = name 
#         self.age = age 
#         self.rollno = rollno

#     def show (self):
#         print('name=',self.name)
#         print('age=',self.age)
#         print('rollno=',self.rollno)
    
# obj = Hod('Arjun',20,101)
# obj.show()



# class New :
#     def __init__(self):
#         self.a = 10 
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# obj1.a = 20 
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)




#declaring instance variable outside a class by using object 

# class Student :
#     def __init__(self): #constructor 
#         self.s_name = "atharv"
#         self.s_rollno = 101 # declaring a instance var inside a constructor 
    
#     def getdata(self):
#         self.s_mb = 1234567890

# obj = Student()
# obj.getdata()
# del obj.s_mb        # deleting the instance variable using obj 
# obj.s_branch = "CSE"   #adding instance variable by using object 
# print(obj.__dict__) 



class New :
    a = 10 
    def __init__(self):
        self.name="Atharv" #instance variable 

obj1 = New()
obj2 = New()
obj3 = New()
print(obj1.name)
print(obj2.name)
print(obj3.name)
New.a = 50 
print(obj1.a)
print(obj2.a)
print(obj3.a)