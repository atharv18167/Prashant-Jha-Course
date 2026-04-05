# n1 = int(input("enter first value:"))
# n2 = int(input("enter second value:"))
# try :
#     print(n1/n2)
# except :
#     print("cannot divide by zero")

# print("To be continued")


# try :
#     n1 = int(input("enter first value :"))
#     n2 = int(input("enter second value :"))
#     print(n1/n2)
# except ZeroDivisionError :
#    print("cannot divide by zero:")
# except ValueError :
#     print("Enter only integer value:")

# print("To be continued")




#hanling multiple diffreent kinds of exeception with 
#single except block 

# try:
#     a=int(input("enter first value:"))
#     b=int(input("enter second value:"))
#     print(a/b)
# except(ValueError,ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# except:
#     print("this is default part of except block")


# try:
#     a=int(input("enter first value:"))
#     b=int(input("enter second value:"))
#     print(a/b)
# except(ValueError,ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# except:
#     print("this is default part of except block")
# else:
#     print("Everything is ok")



#finally block execution
# try :
#     a=int(input("enter first integer no :"))
#     b=int(input("enter second integer no :"))
#     print(a/b)
# except(ValueError,ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# finally:
#     print("this is finally block")


#nested try except block 
# try :
#     a = int(input("enter first integer no :"))
#     b = int(input("enter second integer no :"))
#     try :
#         print(a/b)
#     except ZeroDivisionError as msg :
#         print(msg)
# except ValueError as msg :
#     print(msg) 


try :
    a = int(input("enter first integer no :"))
    b = int(input("enter second integer no :"))
    print(a/b)
except ZeroDivisionError as msg :
        print(msg)
else :
        print("there are no error in try block ")
finally :
        print("i am finally block i always exceute wheater error occurs or not")