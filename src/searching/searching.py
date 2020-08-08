# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        return -1

    # find the middle index
    mid = (start + end) // 2

    # check if the target is the middle index
    if target == arr[mid]:
        return mid
    
    # check if the target is on the left side of the array
    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    
    # check if the target in on the right side of the array
    if target > arr[mid]:
        return binary_search(arr, target, mid + 1, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

