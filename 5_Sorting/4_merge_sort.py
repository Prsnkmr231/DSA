# arr = [1,4,3,2,6,8,9,7]

"""
Problem Statement: Sort the array using merge sort algorithm
"""

"""
Explanation:

it uses the combination of divide and merge.
Initially low = 0
        high = len(arr)-1
We are going to split the array into two halfs, based on the indexes.

mid = (low+high)//2
first half = (low,mid),second_half = (mid+1,high)
it splits the array into two halfs, Sometimes first half will be large than or equal to second half.

After that, we are going to apply the mergesort for the first half using recursion. Internally this call many recursion functions
until the splitting make low==high

for the second half , we are going to apply the mergesort.In this also internally it applies many recursion functions,until the 
splitting make low==high

once the two halfs are sorted then we are going to apply the merge function for adding the two arrays into a single array.


time complecity of the above algorithm is O(Nlog2N),space complexity of the algorithm is O(N)

"""


arr = [1,2,2,3,4,1,3,4,4]


def merge(nums,low,mid,high):

    print(f"nums is : {nums}")
    temp = []
    left = low
    right = mid+1

    while (left<=mid and right<=high):
        if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1

    while left<=mid:
        temp.append(nums[left])
        left+=1
    
    while right<=high:
        temp.append(nums[right])
        right+=1
    
    for i in range(len(temp)):
        nums[low+i]=temp[i]

 



def merge_sort(arr,low,high):

    if low==high:
        return 
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr




low = 0
high = len(arr)-1
# mid = (low+high)//2
temp_array = merge_sort(arr,low,high)

print(temp_array)








# First Function call:
# --------------------

# arr = [1,2,2,3,4,1,3,4,4]

# low = 0, 
# high = 9
# mid  =(0+9)//2 = 4
# first_half = [1,2,2,3,4]
# second_half = [1,3,4,4]

# Second Function Call:
# ----------------------


# arr = [1,2,2,3,4,1,3,4,4]

# low = 0
# high = 4
# mid = (0+4)//2 = 2

# first_half = [1,2,2]
# second_half = [3,4]


# Third_function call:
# ===================

# low = 0
# high = 2
# mid = (0+2)//2 == 1

# first_half = [1,2]
# second_half = [2]

# fouth function call:
# --------------------

# low = 0
# high = 1
# mid = (0+1)//2 == 0

# first_half = [1]
# second_half = [2]


# fifth function call:
# -------------------

# low =0
# high = 0 

# return none.

# execution goes to second merge_sort function


# then second merge_sort function comes into the picture

# here 

# Second_Function_first call:
# --------------------------

# low = 0
# high = 1

