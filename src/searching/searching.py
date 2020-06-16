def linear_search(arr, target):
    # Your code here
    for index,value in enumerate(arr):
        if target == value:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (high + low)//2
    # Your code here
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid -1
        else:
            return mid

    return -1  # not found
