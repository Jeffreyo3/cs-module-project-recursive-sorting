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

# def agnostic_binary_search(arr, target):
    # start = arr[0]
    # end = arr[-1]
    # if len(arr) == 1:
    #     # print("one item")
    #     # print(arr[0])
    #     if arr[0] == target:
            
    #         return arr[0]
    #     else: return -1

    # elif end > start:
    #     # print("End is bigger")

    #     middle = (0 + (len(arr)-1)) // 2
    #     # print(arr[middle])
    #     guess = arr[middle]
        

    #     if target > guess:
    #         if len(arr) == 2:
    #             result indx = agnostic_binary_search(arr[middle+1:], target)
    #             return indx + middle+1
    #         # print(arr)
    #         return agnostic_binary_search(arr[middle:], target)
            

    #     elif target < guess:
    #         # print(arr)
    #         return agnostic_binary_search(arr[:middle], target)
            
    #     else:
    #         # return guess
    #         return middle
        
    # else:
    #     # print("Beginning is bigger")

    #     middle = (0 + (len(arr)-1)) // 2
    #     # print(arr[middle])
    #     guess = arr[middle]
        

    #     if target < guess:
    #         if len(arr) == 2:
    #             return agnostic_binary_search(arr[middle+1:], target)
    #         # print(arr)
    #         return agnostic_binary_search(arr[middle:], target)
            

    #     elif target > guess:
    #         # print(arr)
    #         return agnostic_binary_search(arr[:middle], target)
            
    #     else:
    #         # return guess
    #         return middle

text = "***********************"
def agnostic_binary_search(arr, target):
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1

    start = arr[0]
    end = arr[-1]
    a_idx = 0
    b_idx = len(arr)-1

    while b_idx - a_idx >= 0:
        # ASCENDING SORTED LIST
        if end > start:
            middle = (a_idx + b_idx) // 2

            guess = arr[middle]
            
            if target == guess:
                return middle
            if b_idx - a_idx == 1:
                if arr[b_idx] == target:
                    return b_idx
                else:
                    return -1
            else:
                if target > guess:
                    a_idx = middle

                else:
                    b_idx = middle
                
            
        # DESCENDING SORTED LIST
        else:
            middle = (a_idx + b_idx) // 2

            guess = arr[middle]
            

            if target == guess:
                return middle

            if b_idx - a_idx == 1:
                if arr[b_idx] == target:
                    return b_idx
                else:
                    return -1
            else:
                if target < guess:
                    a_idx = middle
                    
                else:
                    b_idx = middle

    
    return -1
    


# oneItem = [1]
# print(agnostic_binary_search(oneItem, 1))

# tenList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sixList = [1, 2, 3, 4, 5, 6]
# print(f"SEARCH RESULT: {agnostic_binary_search(tenList, 6)}")
# print(f"SEARCH RESULT: {agnostic_binary_search(sixList, 6)}")

# decTenList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# decSixList = [6, 5, 4, 3, 2, 1]
# print(f"INVERSED SEARCH RESULT: {agnostic_binary_search(decTenList, 1)}")
# print(f"INVERSED SEARCH RESULT: {agnostic_binary_search(decSixList, 1)}")

# print(f"OUT OF RANGE SEARCH RESULT: {agnostic_binary_search(tenList, -11)}")
# print(f"OUT OF RANGE INVERSED SEARCH RESULT: {agnostic_binary_search(decTenList, -11)}")


# ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
# descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

# print(f"ascending SEARCH RESULT: {agnostic_binary_search(ascending, 12)}")
# print(f"ascending SEARCH RESULT: {agnostic_binary_search(ascending, 54)}")
# print(f"ascending SEARCH RESULT: {agnostic_binary_search(ascending, 31)}")

# print(f"descending SEARCH RESULT: {agnostic_binary_search(descending, 49)}")
# print(f"descending SEARCH RESULT: {agnostic_binary_search(descending, -17)}")
# print(f"descending SEARCH RESULT: {agnostic_binary_search(descending, -1)}")