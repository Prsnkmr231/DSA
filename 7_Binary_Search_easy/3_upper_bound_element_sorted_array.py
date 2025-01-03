
arr = [3,5,7,8,9,10,12,14,17,19,22,24]


target = 19


"""
Upper Bound Definition:

Find the smallest index such that the element at that index is greater than target
"""


def upper_bound_brute(arr,target):
    ans = len(arr)
    for index in range(len(arr)):
        if arr[index]>target:
            return index
    return ans

upper_bound = upper_bound_brute(arr,18)
print(f"upper bound using brute force is {upper_bound}")



"""
Above approach is brute force approach for finding the upper bound.time complexity of the algorithm is O(N)

"""


def upper_bound_binary(arr,target):

    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>target:
            ans = mid
            high = mid-1
        else:
            low=mid+1

    return ans

ub_binary = upper_bound_binary(arr,7)

print(f"upper bound using binary  is {ub_binary}")



"""
Above approach is using binary search for finding the upper bound.Time complexity of the algorithm i log2N

"""







