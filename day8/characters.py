  #findall() function 

import re
mtch = re.findall('[0-9]',"abch3hdh5bkl@zq%&")
print(mtch)




#sub() function
# this function perform the substitution operation or replacement 
# re.sub(expression,replacement,string) here every match pattern will be replaced by provided replacement
# import re
# obj = re.sub('[a-zA-Z]','*',"2345 ABCD Fach deff")
# print(obj)




#subn()Function
'''it is as similar as sub() function only one thing is diffrent
that is also return number of replacement.This return in tuple where first
element is string and second one is number of replacement'''

#split() function
'''this function is used to split the given string as per the 
some pattern then we should use split()'''


#subn() 
# import re
# obj = re.subn('[0-7]','@','ab3gh6ghhk7')
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacement=",obj[1])

#wap to check the valid mo number 
# import re 
# mo = input("enter mobile number:")
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")



# import re 
# email = input("enter email:")
# obj = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",email)
# if obj!=None:
#     print("valid email")
# else:
#     print("invalid email")







#write a program to check weatherr the given file exists or not
#if it is avavilable then print its content?
import os,sys
fname = input("enter file name:")
if os.path.isfile(fname):
    print("File exists",fname)
    f=open(fname,"r")
else:
    print("File does not exists",fname)
    sys.exit(0)

print("The content of the file is:")
data=f.read()
print(data)