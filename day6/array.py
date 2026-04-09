
list = []
for i in range(int(input("enter the size of array:"))):
    list.append(int(input("enter the element:")))
even = []
for i in list :
    if i % 2 == 0 :
        even.append(i)
print(even)

odd = []
for i in list :
    if i%2!=0:
        odd.append(i)
print(odd)
print("arranged Numbers are :",even+odd)