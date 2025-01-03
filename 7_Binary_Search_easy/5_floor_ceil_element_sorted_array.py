arr = [3,5,7,8,9,10,12,14,17,19,22,24]

"""
Problem Statement:

Floor - represents the largest number <= target (we are implementing in this)

Ceil - represents the smallest number >=target (equals to  lower bound,find the lower bound implementation)

"""
def binary_search_optimal(arr,target):

    low =0
    high = len(arr)-1
    ans =-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=target:
            ans=mid
            low = mid+1
        else:
            high = mid-1
    return ans


floor_index = binary_search_optimal(arr,9)

print(f"floor using binary search is : {floor_index}")