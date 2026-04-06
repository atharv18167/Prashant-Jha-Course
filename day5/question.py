import sys 

class CRUD :
    def __init__(self):
        print("Student Management System")
        self.studentID = []
        self.studentName = []
        self.studentRollNo = []
        self.studentCity = []

    def addstudent(self):
        self.studentID.append(int(input("Enter Student ID :")))
        self.studentName.append(input("Enter Student Name :"))
        self.studentRollNo.append(int(input("Enter Student Roll No :")))
        self.studentCity.append(input("Enter Student City :"))
        print("Student Added Successfully !")
        print()

    def showstudent(self):
            print(f"{'ID':<10}{'Name':<10}{'Roll No':<10}{'City':<10}")
            for i in range(len(self.studentID)):
                print(f"{self.studentID[i]:<10}{self.studentName[i]:<10}{self.studentRollNo[i]:<10}{self.studentCity[i]:<10}")
    
    def updatestudent(self):
        id = int(input("Enter Student ID :"))
        index = self.studentID.index(id)
        print("1.update name")
        print("2.update roll no")
        print("3.update city")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            self.studentName[index] = input("Enter Student Name :")
        elif choice == 2:
            self.studentRollNo[index] = input("Enter Student Roll No :")
        elif choice == 3:
            self.studentCity[index] = input("Enter Student City :")
        else :
            print("Invalid Choice")
        print("Student Updated Successfully !")
        print()
    
    
    
    
    
    def deletstudent(self):
        id = int(input("Enter Student ID :"))
        if id in self.studentID:
            index = self.studentID.index(id)
            print(f"ID:{self.studentID[index]} Name:{self.studentName[index]} Roll No:{self.studentRollNo[index]} City:{self.studentCity[index]}")
            print("Are you sure to delete this student record ?")
            confirm = input().lower()
            if confirm == "yes":
                self.studentID.pop(index)
                self.studentName.pop(index)
                self.studentRollNo.pop(index)
                self.studentCity.pop(index)
                print("Student Deleted Successfully !")
            else :
                print("deletion cancelled !")
        else :
            print("Record not found !")
# obj = CRUD()
# obj.addStudent()
# obj.showstudent()

crud = CRUD()
while True :
    print("1.Add Student:")
    print("2.show student:")
    print("3.delete student:")
    print("4.Exit:")
    print()
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        crud.addstudent()
    elif choice == 2:
        crud.showstudent()
    elif choice == 3:
        crud.deletstudent()
    elif choice == 4:
        sys.exit()

obj = CRUD()
obj.addStudent()
obj.showstudent()
