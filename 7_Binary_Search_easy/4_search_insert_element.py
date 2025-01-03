arr = [3,5,7,8,9,10,12,14,17,19,22,24]

"""
Problem Definition: 

Find the index at which the target element can be inserted.

"""

def search_insert_brute(arr,target):
    ans = len(arr)-1 
    for index in range(len(arr)):
        if arr[index]>=target:
             return index
    return ans
            



brute_index = search_insert_brute(arr,16)

print(f'Index at which element is inserted using brute force apprach are: {brute_index}')

"""
Above approach is brute force approach, time complexity of the algorithm is o(N)
"""




def search_insert_element(arr,target):

    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low<=high:
            mid = (low+high)//2
            if arr[mid]>=target:
                  ans = mid
                  high = mid-1
            else:
                  low = mid+1
    return ans


insert_elem = search_insert_element(arr,14)

print(f"insert_elem using optimal binary search approach is: {insert_elem}")



            