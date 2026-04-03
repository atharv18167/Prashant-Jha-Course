# myList = [['prashant','jha'],['85','56'],[440022,"yyy"]]
# print("example of multidimensinal list : ")
# print(myList)
# print(myList[row][col])
# print(myList[0][0]) #prashant
# print(myList[0][1])
# print(myList[1][0])
# print(myList[2][0])
# print(myList[2][1])

# list1=["prashant","jha"]
# print(list1*2)

# list2 =[50,23.78]
# print(list1+list2)

# list2 =[50,23.78,'prashant']
# del list2[2]
#del list2
# print(list2)

# list2 =[50,23.78,'prashant']
# list2.clear()
# print(list2)
# name = "prashant"
# print(name)
# myname = list(name)
# print(myname)


# mylist =[40,30,50,60]
# mylist.reverse()
# print(mylist)


#sorting 
# mylist = [40,25,94,67,98]
# mylist.sort()
# print(mylist)
#default sorting order for number is acending order 
# deafault sorting order for string is alphabetic order 
# we sjould know that list should contain homogenious 
# data othervise we will get typeerror 

 

# alising 
# mylist =[44,22,56,78,23]
# newlist = mylist #assigning the addresss 
# print(id(mylist))
# print(id(newlist))
# mylist[0]="prashant"
# print(mylist)
# print(newlist)



# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,7,9,11],
#        [34,12,67,43]]

# for i in range (0,4):
#     print(arr[i].pop())


# arr =[1,2,3,4,5,6]
# for i in range (1,6):
#     arr [i-1] = arr [i]
# for i in range (0,6):
#     print(arr[i],end = " ")


# a=[1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50
# print(a)

a=[1,2,3,4,5]
print(a[3:0:-1])