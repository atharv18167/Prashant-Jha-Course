#reverse dictionary 

a = {"C":3, "B":3 , "A":1}
sorted_dict= dict(sorted(a.items()))
print(sorted_dict)

print("Descending order")
sorted_dict= dict(sorted(a.items(),reverse=True))
print(sorted_dict)

