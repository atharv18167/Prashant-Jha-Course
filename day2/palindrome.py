name = input("enter the string : ")
print(name)
print(name[::-1])

if name == name[::-1] :
    print("it is a palindrome")
else:
    print("it is not a palindrome")