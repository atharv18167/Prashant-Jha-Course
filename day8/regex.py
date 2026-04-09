import re #re module for performing all the regular expression based 
# count = 0 #to count the number of matching found
# pattern = re.compile("function") #string converts into bytecode
# #print(pattern)
# matcher = pattern.finditer("A function in python is defined by a def keyword and the function is called as the name of function ")
# #print(matcher)
# for i in matcher :
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences:" , count)





# import re #re module for performing all the regular expression based 
# count = 0 #to count the number of matching found
# matcher = re.compile("Hi","HiHiHiHi") #string converts into bytecode
# #print(pattern)
# # matcher = pattern.finditer("A function in python is defined by a def keyword and the function is called as the name of function ")
# #print(matcher)
# for i in matcher :
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences:" , count)





import re 
obj = input("enter any character:")
objmatch=re.finditer(obj,"a7b @k9z")
#print(objmatch)
for match in objmatch:
    print(match.start(),"...",match.end(),"...",match.group())