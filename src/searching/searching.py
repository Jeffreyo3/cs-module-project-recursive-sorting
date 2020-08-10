# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    else:
        middle = (start + end) // 2

        guess = arr[middle]
        

        if target > guess:
            return binary_search(arr, target, (middle + 1), end)
            

        elif target < guess:
            return binary_search(arr, target, start, (middle -1 ))
            
        else:
            return middle
    
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    # Your code here
    pass

