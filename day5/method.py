#static method 
#instance method
#class method

#instance method 
# class Student :
#     def __init__(self,name,rollno,mob):
#         self.name= name #instamce method 
#         self.rollno = rollno
#         self.mob = mob
#     def display(self): #instance method
#         print(self.name,"",self.rollno,"",self.mob)
# stud = Student("prashant",101,1234567890)
# stud.display()


#static method 
class Student :
    #by using class name we can access static method 
    @staticmethod #decorator
    def get_personal_detail(firstname,lastname):
        print("your personal details=",firstname,lastname)

    @staticmethod
    def contact_detail(mobile_no,rollno):
        print("your contact detail=",mobile_no,rollno)

Student.get_personal_detail("Atharv","Satardekar")
Student.contact_detail(1234567890,101)