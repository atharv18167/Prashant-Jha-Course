#extending property from om=ne class to another class is called as a inheritance 
#base class : class which inherits its property to another class is called as a base class or parent class
#derived class : a class which properties are inherited called as derived or child class

#types :1. single inheritance
#        2. multiple inheritance
#        3. multilevel inheritance
 
#single inhertance : one base class and one derived class , Syntax : class derived-class(base-class):


#single inheritance 
# class College : #parent class 
#     def college_name(self): #
#         print("college name is YBIT") # member function of college  

# class Student(College):
#     def student_info(self):
#         print("Name: Harshad (nana)")
#         print("Branch: PEON")
# obj = Student() #object create child class 
# obj.college_name()
# obj.student_info()



#multilevel inheritance
# class College :
#     def college_name(self):
#         print("college name is YBIT")

# class Student(College): #second class second-level
#     def student_info(self):
#         print("Name: Harshad (nana)")
#         print("Branch: PEON") 

# class Exam(Student):
#     def subject(self):
#         print("subject1: Design Engineering")
#         print("subject2: Civil Engineering")
#         print("subject3: Mechanical Engineering")
# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()




#multiple inheritance 
class SubjMarks:
    math =int(input("Enter paper marks of math:"))
    DE = int(input("Enter paper marks of DE:"))
    C = int(input("Enter paper marks of C:"))
    english = int(input("Enter paper marks of english:"))

class PractMarks :
    cpract = int(input("Enter practical marks of c:"))

class Result(SubjMarks, PractMarks):
    def total(self):
        if self.math>=40 and self.DE>=40 and self.C>=40 and self.english>=40 and self.cpract>=20:
            print("Result: PASS")
        else :
            print("Result: FAIL")
obj = Result()
obj.total()