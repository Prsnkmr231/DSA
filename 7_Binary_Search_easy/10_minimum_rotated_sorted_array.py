nums = [4,5,6,0,1,2,3]

"""
Problem Statement:

Find the  minimum element in the rotated sorted array
"""



"""
Below mentioned approach is the brute force approach. time complexity of the algorithm is O(n)

we go through each and every element and finds out the minimum element.
"""

def brute_minimum(nums):
    max_value = float('inf')
    for element in nums:
        if element<max_value:
            max_value = element
    return max_value

minimum_element = brute_minimum(nums)

print(f"minimum element in the rotated sorted array using brute force is: {minimum_element}")




"""
below mentioned approach is the most optimal approach using binary search.time complexity of the algorithm is O(log2N)


Note: In a rotated sorted array one half of the array is always sorted.

process:

1.find out the mid value
2.check the left half is sorted ,if it is 
3.In a sorted array always the smallest index has the minimum element based on this we will assign the value after checking the 
  consition that the lowest index is less than the answer.Update the low to mid+1
4.In the other half find the lowest index element and check the element is less than or ans if it is replace the ans value.
  whatever it may be update the value of high to mid-1

"""


def optimal_minimum(nums):

    low = 0
    high = len(nums)-1
    ans = float('inf')

    while low<=high:
        mid = (low+high)//2

        if nums[low]<=nums[mid]:
            if nums[low]<ans:
                ans = nums[low]
            low = mid+1
        else:
            if nums[mid]<ans:
                ans = nums[mid]
            high = mid-1

    return ans

minimum_optimal = optimal_minimum(nums)

print(f"minimum element in the nums array using binary search is {minimum_optimal}")

        
