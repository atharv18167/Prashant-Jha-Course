mylist= [5,7,8,3,7,8,9,2,3]
newlist =[]

for i in range (len(mylist)):
    count = 0
    key = mylist[i]

    j =i+1
    while j <len(mylist):
        if key == mylist[j]:
            newlist.append(key)
        j = j+1
print(len(newlist))