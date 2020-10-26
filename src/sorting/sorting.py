# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # create a list with lenght
    # equal to total incoming elemnts
    merged_arr = [0] * elements 
    a_idx = 0 # keep track of current arrA index
    b_idx = 0 # keep track of current arrB index

    # iterate over merged_arr
    for i in range(len(merged_arr)):
        # check if b_idx is out of range
        if b_idx > len(arrB)-1:
            # all b elements have been sorted and we can now
            # assign the rest of the a elemtns since they're sorted
            merged_arr[i] = arrA[a_idx]
            a_idx += 1
        # check if a_idx is out of range
        elif a_idx > len(arrA)-1:
            # all a elements have been sorted and we can now
            # assign the rest of the b elemtns since they're sorted
            merged_arr[i] = arrB[b_idx]
            b_idx += 1

        # if current indexes are in range
        else:
            # check if a is less than b
            if arrA[a_idx] < arrB[b_idx]:
                # assign current merge_arr idx to a element
                merged_arr[i] = arrA[a_idx]
                a_idx += 1
            else:
                # assign current merge_arr idx to b element
                merged_arr[i] = arrB[b_idx]
                b_idx += 1
    # when all merge_arr elements are set, return final result
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
    # utilize any extra memory
    # In other words, your implementation should not allocate any additional lists 
    # or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

arr1 = [1, 8, 20]
arr2 = [3, 6, 7]
array = [1, 24, 22, 7, 3, 6, 9, 21, 0, 14]
print("\nTEST MERGE")
print(merge(arr1, arr2))

print("\nTEST MERGE_SORT")
print(merge_sort(array))