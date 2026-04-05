import csv 
f = open("result.csv","a",newline="")
a = csv.writer(f)

# a.writerow(["rollno","mobileno","maths","phy","chem","total","percentage","email","result"])
rollno = int(input("enter roll no:"))
mobileno= int(input("enter mobile no:"))
maths = int(input("enter the marks of p1:"))
phy = int(input("enter the marks of p2:"))
chem = int(input("enter the marks of p3:"))
total = maths+phy+chem
percentage = total/3.0
email = input("enter mail:")
result = []
if percentage >=40 :
    result ="pass"
else:
    result ="fail"


a.writerow([rollno,mobileno,maths,phy,chem,total,percentage,email,result])
print("student record has been saved")