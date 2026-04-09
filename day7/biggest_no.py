def findBiggestNumber(array):   
    firstvalue = array[0]       #======> O(1)
    for i in range(1,len(array)): #======> O(n)
        if array[i] > firstvalue: #=====>O(1)
            firstvalue = array[i]  #=====>O(1)
    return firstvalue

array = [1,2,3,4,5]
print(findBiggestNumber(array))  #======> O(1)