def binarySearch(array,target):
    start = 0 
    end = len(array)-1
    while start <=end:
        mid = (start+end)//2
        if array[mid]== target:
            return mid
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1       

array = [1,2,3,4,5,6,7,8,9,10]
target = 4
result = binarySearch(array, target)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)