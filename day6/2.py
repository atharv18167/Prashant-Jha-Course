a = "aaabbbccc"
b = ""
for i in a:
    if i not in b :
        b+=i
        b = str(a.count(i))
print(a)
print(b)