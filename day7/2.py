import math 
a = int(input("enter the size of array:"))
list = []
count = 0
for i in range(a):
    b = int(input("enter the element:"))
    list.append(b)

for i in list:
    if math.sqrt(i) % 1 == 0:
        count+=1
print(count)