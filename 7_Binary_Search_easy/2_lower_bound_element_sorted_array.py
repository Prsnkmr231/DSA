

arr = [3,5,7,8,9,10,12,14,17,19,22,24]


"""
Lower Bound:

Find the index so that the element at  that index is greater than or equal to the target


"""




"""
This approach is a brute force algorithm, it will check each and every element for the condition that the element at that index
is greater than or equal to the target.In worst case the time complexity of the algorithm is O(N)
"""


def lower_bound_brute(arr,target):
    ans = len(arr)
    for index in range(len(arr)):
        if arr[index]>=target:
            return index
    return ans
print(f"lower_index is : {lower_bound_brute(arr,17)}")



"""
This approach is a binary search algorithm, it checks the condition using binary search  and finds out the index at which the 
element is greater than or equal to the target. In this approach the time complexity of the algorithm is O(log2N)
"""


def lower_bound_binary(arr,target):
    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=target:
            ans=mid
            high = mid-1
        else:
            low = mid+1
    return ans

print(f"lower index using binary search is: {lower_bound_binary(arr,17)}")




