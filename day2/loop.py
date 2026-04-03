# #for loop 
# for i in range (1,11) :
#     print(i)

# for i in range (1,11):
#     print (i*2,"\t",i*3,"\t",i*4,"\t",i*5,"\t",i*6,"\t",i*7,"\t",i*8,"\t",i*9,"\t",i*10)
# print("__________________________________________________________________________")
# print()
# for i in range (1,11):
#     print (i*11,"\t",i*12,"\t",i*13,"\t",i*14,"\t",i*15,"\t",i*16,"\t",i*17,"\t",i*18,"\t",i*19,"\t",i*20)



#wap to remove the duplicate of the string 
# name = "racear"
# newname =""
# for i in name :
#     if i not in newname :
#         newname = newname +i
# print(name)
# print(newname)


# for i in range (5,0,-1) :
#     print(i)

# for i in range (10,0,-2):
#     print(i)


#wap reverse string using for loop
name = "prashant"
n = len(name)
newname = ""
for i in range (n,0,-1) :
    newname = newname + name[i-1]
print(name)
print(newname)