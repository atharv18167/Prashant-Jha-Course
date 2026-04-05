name = "programming"
vowels = ['a','e','i','o','u']
cons = 0 
vowel = 0 
for i in name : #i=0:p
    if i in vowels :
        vowel+=1
    else :
        cons+=1
print("consonents=",cons)
print("vowels=",vowel)