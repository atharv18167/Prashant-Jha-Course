# mytuple = ("prashant", "ashish", "rahul", "sandip", "komal", "ankush" , "rajesh", 23,3.15,77,"sandip")

# print(mytuple)
# print(type(mytuple))

# mytuple[2] ="sunil"
# print(mytuple)

# init_tuple = ()
# print(init_tuple.__len__())

# init_tuple_a = 'a' , 'b'
# init_tuple_b = ('a' , 'b')
# print(init_tuple_a == init_tuple_b)

# init_tuple_a = '1' , '2'
# init_tuple_b = ('3' , '4')
# print(init_tuple_a + init_tuple_b)

# init_tuple = ('python',) *3
# print(type(init_tuple)) 

# init_tuple =(1,) *3
# init_tuple [0] = 10  # This will raise an error because tuples are immutable
# print(init_tuple)

# init_tuple = ((1,2),) *7 
# print(len(init_tuple[3:8]))


# names = [4,2,5,6,8,2]
# for i in names : #i= 6:2
#     print (i)


# names = [4,0,2,5,0,1]
# for i in names : #i= 6:2
#     if i == 0:
#         names.remove(i)
#         names.append(i)
# print(names)


# A = [1,2,2,3,4,4,5]
# newlist = []
# for i in A :
#     if i not in newlist :
#         newlist.append(i)
# print(newlist)


# A = [1,2,3] 
# B =[2,3,4] 
# C =[3,4,5]
# for i in A :
#     if i in B and i in C :
#         print(i) 



n = int(input("enter the array size :"))
arr = []
for i in range (n) :
    val = int(input("enter the value :"))
    arr.append(val)
sum = 0 
print(arr) 
for i in range (n) :
    if i +1 in range (n) :
        sum += abs (arr[i] - arr[i+1])
print(sum)
    