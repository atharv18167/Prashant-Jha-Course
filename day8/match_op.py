#match () function operation
# import re
# a = input("enter string to perform match operation:")
# mtch = re.match(a,"Python is very important language")
# print(mtch)
# if mtch!= None :
#     print("Match found at beginning level")
#     print(mtch.start()," " ,mtch.end())
# else:
#     print("there is no matching at beginning level")

#fullmatch function
''' as a name suggest when we have to match full string with the 
given pattern then we have to use fullmatch() function.
if match is done then we will get match object else we will get None'''

#fullmatch()
import re #re module for performing all the regular expression based 
a = input("enter string to perform match operation:")
mtch = re.fullmatch(a,"pythonisvery") #string converts into bytecode
print(mtch)
if mtch!= None :
    print("Match found at beginning level")
    print(mtch.start()," " ,mtch.end())
else:
    print("full match not found")