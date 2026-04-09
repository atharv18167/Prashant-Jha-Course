a = "gasgg54@#vscsd!s*"
count = 0



# for i in a :
#     if not i.isalnum():
#         count+=1
# print(count)

for i in a :
    z = ord(i)
    if z>=97 and z<=122:
        continue
    elif z>=48 and z<=57:
        continue 
    else :
        count+=1
print(count)