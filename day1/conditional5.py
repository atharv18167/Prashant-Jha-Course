phy = int(input("enter you marks:"))
chem = int(input("enter you marks:"))
maths = int(input("enter you marks:"))
total = phy + chem + maths 
print ("total:",total)
percent = total/3.0 
print("percent:",percent)
gender = input("enter gender:")
if percent >=60 and gender=="male ":
    print ("eligible to placement:")
else :
    print ("eligible to data entry ")