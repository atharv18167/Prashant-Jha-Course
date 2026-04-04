# # def msg (): #called function 
# #     print ("hello world welcome to python programming")
# # msg () #calling function 
# # msg ()

# def arthmetic ():
#     a = int(input("enter the value of a:"))
#     b = int(input("enter the value of b:"))
#     add = a+b 
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div

# # print(arthmetic ()) # calling function 
# result = arthmetic () # calling function
# print ("Arithmetic=",result)


#how many type of argument pass in function 
#1. positional argument
#2. keyword argument
#3. default argument
#4. variable number of argument / variable length argument 



#postional argument
def login (username,password) :
    if username == password :
        print ("login successful")
    else :
        print ("invalid credentals")

username = input("enter username :")
password = input("enter password:")
login (username,password) #calling function  