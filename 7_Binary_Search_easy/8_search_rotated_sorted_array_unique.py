
nums = [7,8,9,1,2,3,4,5,6]




"""
Problem Statement: Find out the index of the target element in the rotated sorted array.

"""


"""
Below mentioned approach is the brute force appraoch. In this we are going to use linear search to find the index of the target element.
time complexity of the algorithm is O(N)
"""


def search_brute(nums,target):
    for index in range(len(nums)):
        if nums[index]==target:
            return index
        


index_brute = search_brute(nums,1)
print(f"index of the target element using brute force approach is: {index_brute}")


"""
Below mentioned approach is the optimal approach.In this case we are going to use binary search because we are searching for a element in 
a sorted array.Time complexity of the algorithm is O(log2N)


Process:

1.find out the mid value.
2.check the mid element is equal to target
3.check the left half is sorted if it is,
      check the element lies between low and mid index if it is
          update high
      else 
          update low

4.else the right half is sorted if it is,
      check the element lies between mid and high index if it is
          update low
      else
          update high

 

"""
        #  0 1 2 3 4 5 6
nums1 = [4,5,6,7,0,1,2]

def search_binary(nums,target):
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            
            if nums[low]<=nums[mid]:
                if target<nums[mid] and target>=nums[low]:
                    high = mid-1
                else:
                    low = mid+1

            else:
                if target>nums[mid] and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

        
index_binary = search_binary(nums1,0)

print(f"index of the element using binary_search is {index_binary}")

        
