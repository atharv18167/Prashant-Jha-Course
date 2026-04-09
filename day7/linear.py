def linearSearch(array,target): #[1,2,3,4,5,6,7,8,9,10]
    for i in range(len(array)): #i=3
        if array[i] == target: #4==4
            return i 
    return -1

array = [1,2,3,4,5,6,7,8,9,10]
target = 4
result = linearSearch(array, target)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)