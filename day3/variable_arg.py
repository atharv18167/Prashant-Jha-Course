#variable length argument

# def nameofCitys(*city):
#     print("City Name's=",city)

# nameofCitys("Pune","Mumbai","Banglore")

#wap to menu driven code 
import sys 
def add():
    val1 = int(input("enter the value of val1:"))
    val2 = int(input("enter the value of val2:"))
    print("Add=",val1+val2)

def sub() :
    val1 = int(input("enter the value of val1:"))
    val2 = int(input("enter the value of val2:"))
    print("Substraction=",val1-val2)

def mul():
    val1 = int(input("enter the value of val1:"))
    val2 = int(input("enter the value of val2:"))
    print("mul=",val1*val2)
    
def div():
    val1 = int(input("enter the value of val1:"))
    val2 = int(input("enter the value of val2:"))
    print("div=",val1/val2)
    

while True :
    print("1.Addition ")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3 :
        mul()
    elif choice == 4 :
        div()
    elif choice == 5:
        sys.exit()