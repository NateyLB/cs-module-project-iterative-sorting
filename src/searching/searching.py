def linear_search(arr, target):
    # Your code here
    ##interate through indexes of arr
    for index,value in enumerate(arr):
        #if value of array == targter value, return index
        if target == value:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #set a low, and high to keep track of both ends of the arr
    low = 0
    high = len(arr)-1
    #if low does not pass high
    while low <= high:
        #get mid point
        mid = (high + low)//2
    # Your code here
    #if target is greater than midpoint
        if arr[mid] < target:
        #throw away the lower half
            low = mid + 1
        #if target is less than midpoint
        elif arr[mid] > target:
        #throw away upper half
            high = mid -1
        else:
        #if midpoint = target, return the index
            return mid

    return -1  # not found
