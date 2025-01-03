
arr = [7,8,9,1,2,3,3,4,5,6]

arr1 = [3,1]


"""
Problem Statement: Find out that the given target element exist in the rotated sorted array with duplicates.
"""


"""
if you are looking for brute force approach please refer the previous file
"""


def search_binary_duplicates(nums,target):
        low = 0
        high = len(nums)-1

        print(low)
        print(high)

        while low<=high:
            print("while executing")
            mid = (low+high)//2
            print(f"mid value is {mid}")
            if nums[mid]==target:
                print("first if executing")
                return True
            
            if (nums[low]==nums[mid]) and (nums[mid]==nums[high]):
                print("if executing")
                low = low+1
                high = high-1
                continue
            
            elif nums[low]<=nums[mid]:
                print("elif is executing")
                if target<nums[mid] and target>=nums[low]:
                    high = mid-1
                else:
                    low = mid+1

            else:
                if target>nums[mid] and target<=nums[high]:
                    low = mid+1
                    print("else is executing")
                else:
                    high = mid-1
                
        return False


checker = search_binary_duplicates(arr1,1)

print(f"the checker value is {checker}")