a = [-1,2,-3,4,5,-6]
positive = []
negative = []
for i in a :
    if i > 0 :
        positive.append(i)
    else :
        negative.append(i)
# print("positive numbers are : ", positive,negative)
# print("negative numbers are : ", negative)
for i in range (len(negative)) :
    a[i*2] = negative[i]
    a[i*2 + 1] = positive[i]
print(a)