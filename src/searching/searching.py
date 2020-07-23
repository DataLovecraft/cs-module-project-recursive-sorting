# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid+1, end)


def agnostic_binary_search(arr, target):
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True

    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    else:
        return binary_search(arr, target, len(arr) - 1)
