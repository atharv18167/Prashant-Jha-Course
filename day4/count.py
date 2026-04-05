s = [1,2,2,3,4,3,5]
k ={}

for i in s:
    if i in k :
        k[i]+=1
    else :
        k[i] = 1
print (k) 
