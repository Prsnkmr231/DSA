nums = [4,5,6,0,1,2,3]

nums1 = [0,1,2,3,4,5,6]

"""
Problem Statement:

Find how many times the array is rotated
"""



"""
Below mentioned approach is the brute force approach. time complexity of the algorithm is O(n)

we go through each and every element and finds out the minimum element.In a rotated sorted array number of times the array is 
sorted is equal to the index of the minimum element.



"""

def brute_minimum(nums):
    min_value = float('inf')
    index = -1
    for i in range(len(nums)):
        if nums[i]<min_value:
            min_value = nums[i]
            index = i
    return index

minimum_element_index = brute_minimum(nums1)
print(f"times sorted array is rotated: {minimum_element_index}")




"""
Below mentioned approach is the optimal approach using binary search, time complexity of the algorithm is O(log2N)

it finds out the minimum element, once it finds out we can get the index
"""


def optimal_binary(nums):
    low = 0
    high = len(nums)-1
    ans = float('inf')
    index =-1

    while low<=high:
        mid = (low+high)//2


        if nums[low]<=nums[high]:
            if nums[low]<ans:
                ans = nums[low]
                index = low
                break


        if nums[low]<=nums[mid]:
            if nums[low]<ans:
                ans = nums[low]
                index = low
            low = mid+1
        else:
            if nums[mid]<ans:
                ans = nums[mid]
                index = mid
            high = mid-1

    return index



times_rotated = optimal_binary(nums1)

print(f"number of times array is rotated: {times_rotated}")