# #search() function
# #if the match found anywhere in the string then it return object else it will return none 
# import re
# a = input("enter string to perform search operation:")
# mtch = re.search(a,"python sss dynamic lann")
# print(mtch)
# if mtch!= None :
#     print(mtch.start()," ",mtch.group())
# else:
#     print("there is no matching anywhere")



import re
a = input("enter string to perform search operation:")
f = open('py.txt','r')
c = f.read()
mtch = re.search(a,c)
print(mtch)
if mtch!= None:
    print("match found at beginning level:")
    print(mtch.start()," ",mtch.end())
else:
    print("there is no matching at beginning level")


#==========================================================================================#
#match character classes
#[abc]=====> Either a or b or c
#