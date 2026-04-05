# f = open("myfile.txt","w")
# print("name of file :",f.name)
# print("file mode :",f.mode)
# print("readable :",f.readable())
# print("writeable:",f.writable())
# f.close()
# print("fle closed:",f.closed)


# ##performing write operation
# f = open ("myfile.txt","a") #w = override the sentence ,  #a = append or add the next sentences 
# f.write("\n sawantwadi is a smart city ")
# f.write("\n vengurla is a smart city ")
# f.write("\n zirangwadi is a smart village ")
# f.close()
# print("file operation is done")


#inserting the list 
# f = open("myfile.txt","w")
# mylist = ["prashant" , "mahesh" , "suresh"]
# tuple = ("harshad" , "nana")
# dict = [{"name" : "prashant" , "age" : 20} , {"name" : "ashish" , "age" : 22}]
# f.writelines(mylist)
# f.writelines(tuple)
# f.writelines(dict)
# f.writelines(dict)
# f.close()
# print("file operation is done")



# # reading data from a file 
# f = open("myfile.txt","r")
# print(f.read())
# f.close()


#with statement block '
# with open("myfile.txt","w") as f:
#     f.write("amit/n")
#     f.write("nana/n")
#     f.write("harshad/n")
    # print("file closed:",f.closed)
# print("file closed:",f.closed)


# with open("myfile.txt","r") as f :
#     content = f.read()
#     print(content)



f1=open("jonatan.jpg","rb")
f2=open("rossom.jpg","wb")
data =f1.read()
f2.write(data)
print("new image is available with the name :")