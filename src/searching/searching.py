# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target):
    # Your code here
    # we're searching in between the low and high indices 
    low = 0
    high = len(arr) - 1
​
    # loop so long as low hasn't moved passed high
    while low <= high:
        mid = (low + high) // 2
​
        # base case where we've found our target 
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            # toss out the right side since the target 
            # has to be on the left side 
            # do this by setting high to be mid - 1
            high = mid - 1
        else:
            # toss out the left side since the target
            # has to be on the right side 
            # do this by setting low to mid + 1
            low = mid + 1
​
    return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

