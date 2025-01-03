
arr = [3,5,7,8,9,10,12,14,17,19,22,24]




"""
Definition:

Find a element by searching throughout the array.
"""


"""
Below approach is a linear search throughout the array using a for loop.it is a brute force approach in worst case it takes 
O(N) time complexity

"""

def find_element_brutal(element,arr):
    for index in range(len(arr)):
        if arr[index]==element:
            return index
    return -1


index_brutal = find_element_brutal(19,arr)

if index_brutal!=-1:
    print(f"element is found at index: {index_brutal}")

else:
    print(f"element is not found")


#Above approach is brutal force algorithm it takes O(N) time complexity. to overcome this we can go with below optimal approach

"""
Below Mentioned approach is  optimal solution , it finds out the element in array using binary search.It takes the O(logN)
time complexity 


"""

def find_element_binary(arr,element):
    lower_bound = 0
    upper_bound = len(arr)-1

    while lower_bound<=upper_bound:
        print("executing")
        mid = (lower_bound + upper_bound)//2
        if arr[mid]==element:
            return mid
        elif arr[mid]>element:
            upper_bound = mid-1
        else:
            lower_bound =mid+1

    return -1



optimal_index = find_element_binary(arr,6)

if optimal_index!=-1:
    print(f"element is found at {optimal_index}")
else:
    print(f"element not found")


"""
Below Mentioned approach is recursion based binary search solution, it finds out the element in array using 
recursion based binary search with a time complexity of O(logn)
"""


def find_element_recursion_binary(arr,element,low_bound,upp_bound):
    if low_bound>upp_bound:
        return -1
    
    mid = (low_bound+upp_bound)//2

    if arr[mid]==element:
        return mid
    
    elif arr[mid]>element:
        upp_bound = mid-1
        return find_element_recursion_binary(arr,element,low_bound,upp_bound)
    
    low_bound = mid+1
    return find_element_recursion_binary(arr,element,low_bound,upp_bound)


index_recursion_binary = find_element_recursion_binary(arr,6,0,len(arr)-1)


if index_recursion_binary!=-1:
    print(f"element is found at {index_recursion_binary}")
else:
    print(f"element not found")