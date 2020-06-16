# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # iterate through arr indexes
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # get the minumum value of the array
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        


        # TO-DO: swap
        # Your code here
        # put min value in min index
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # interate through arr indexes
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    """
        - go through every bucket
        - iterate throgh the arr
        - if value in the arr[i] == bucket.index == True, then we increase bucket by 1
        - loop through buckets and take the index from and create a loop with range using the index
    """
    # Your code here
    maximum = 0
    buckets = []
    # get maximum and check for negatives
    for value in arr:
        if value > maximum:
            maximum = value
        elif value<0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            pass
    # create buckets and initialize to zero
    for times in range(0, maximum + 1):
        buckets.append(0)
    # fill buckets
    for index in range(0,len(buckets)):
        for val in arr:
            if val == index:
                buckets[index] += 1
    # clear arr           
    arr = []
    # append sorted values to arr
    for index,value in enumerate(buckets):
        for times in range(value):
            arr.append(index)

    return arr

test_array = [3,0,4,1,10,2,5,7,2,3,2,3,2,2,2]
expected =   [0,1,2,2,3,4,5,7,10]
print(counting_sort(test_array))