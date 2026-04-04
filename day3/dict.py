# mydict = {
#     101 : "prashant",
#     102 : "atharv",
#     "103" : "mohini",
#     "104" : "satyarth",
#     101 : "ashish",
#     104 : "ashish",
# }
# print(mydict)

# with the help of key we have to print th value 
# a = mydict[102]
# print(a)

#we will replace the old value by new value
# mydict[102]="peter"
# print(mydict)

# only print the keys x=0,1
# for x in mydict :
    # print(x)

#only print the values 
# for y in mydict :
#     print(mydict[y])


#printing both key and values 
# for x , y in mydict.items() :
#     print(x,y)


#if i have to ad new key and value pair in dictionary
# mydict["mobile_no"] = 1234567890
# print(mydict)



# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])  # error occurs due to the fact that we are trying to access the value of key'a' and 'b' together which is not possible in a dictionary. We can only access the value of one key at a time. To access the value of key 'a', we can use a['a'] and to access the value of key 'b', we can use a['b'].


# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] +=1

# sum = 0
# for k in arr :
#     sum += arr[k]
# print(sum)


# mydict = {}
# mydict[1] = 1
# mydict['1'] = 2
# mydict[1.0] = 4

# sum = 0 
# for k in mydict :
#     sum += mydict[k]
# print(sum)



# mydict = {}
# mydict[(1,2,4)]= 8
# mydict[(4,2,1)] = 10
# mydict[(1,2)] = 12
# sum = 0
# for k in mydict :
#     sum += mydict[k]
# print(sum)
# print(mydict)



# box = {}
# jars = {}
# crates = {}
# box['biscuit']= 1
# box['cake'] = 3
# jars ['jam'] = 4
# crates ['box'] = box
# crates ['jars'] = jars 
# print(len(crates[box]))



# dict = {'c' : 97 , 'a':96 , 'b':98}
# for _ in sorted(dict) :
#     print(dict[_])

# rec = {"name" : "python " , "age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))
# print((r) == (rec))

# rec = {"name" : "python " , "age":"20"}
# id1 = id(rec)
# del rec
# rec = {"name" : "python " , "age":"20"}
# id2 = id(rec)
# print(id(id1) == id(id2))