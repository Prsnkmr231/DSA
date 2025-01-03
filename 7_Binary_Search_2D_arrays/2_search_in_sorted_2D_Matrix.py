matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


"""
Problem Statement:

        find the element in a sorted 2D array,if the element exists return True else return False.
"""

"""
Below Mentioned Approach is the Brute Force Approach,so it iterates through each and every element in the 2D array, if the element
exists return True,else return False.

Time Complexity of the above algorithm is O(num_rows * num_columns)
"""

target = 8

def brute_force_approach(matrix,target):

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column]==target:
                return True
    
    return False


value = brute_force_approach(matrix,8)


print(f"{target} element exists in the matrix: {value}")




"""
Below Mentioned Approach is the better approach.We are going to use the advantage of sorted array. In this approach for every 
row we are going to check the target element lies between starting and ending element of the array.Once it exists we are going 
to apply the binary search for that  1D array and  if the element exists return True else return False
"""


def binary_optimal(arr,target):
    low =0
    high = len(arr)-1
    while low<=high:

        mid = (low+high)//2
        if arr[mid]==target:
            return True
        elif arr[mid]>target:
            high = mid-1
        
        else:
            low = mid+1

    return False
    

def better_approach(matrix,target):
    
    value = False
    for row in range(len(matrix)):
        if  target>=matrix[row][0] and target<=matrix[row][-1]:
            value = binary_optimal(matrix[row],target)
            print(f"value in binary search is {value}")

    
    return value


value_better = better_approach(matrix,8)
        

print(f"{target} exists in the  matrix: {value_better}")




"""
Below Mentioned approach is optimal approach, we take the advantage of sorted 2D array. we considered it as a hypothetical sorted 1d array and find
out the target element using binary search algorithm.
"""



matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

def Binary_optimal(matrix,target):

    low = 0
    high = len(matrix)*len(matrix[0])-1
    while low<=high:

        mid = (low + high)//2

        row = mid//len(matrix[0])
        column = mid%len(matrix[0])
        if matrix[row][column]==target:
            return True
        elif matrix[row][column]>target:
            high = mid -1
        
        else:
            low = mid+1

    return False


value_optimal = Binary_optimal(matrix,8)


print(f"{target} exists in the matrix : {value_optimal}")








