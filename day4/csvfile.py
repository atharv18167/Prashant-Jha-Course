import csv 
f = open("student.csv","a",newline="")
a = csv.writer(f)
# a.writerow(["studentID","Roll NO","name","Mobile No"])

studentid = int(input("enter student id:"))
rollno = int(input("enter roll no:"))
name = input("enter name :")
mobileno = int(input("enter mobile no:"))
a.writerow([studentid,rollno,name,mobileno])
print("Student record has save")
