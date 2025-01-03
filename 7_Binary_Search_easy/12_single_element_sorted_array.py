arr = [1,1,2,2,3,3,4,5,5,6,6,]
    #    0,1,2,3,4,5,6,7,8,9,10

arr1 = [1,2,2,3,3,4,4,5,5]
        # 0,1,2,3,4,5,6,7,8

"""

Problem Statement:

Find the element which is present only single time in the  sorted array,there is compulsarily exists the single element and for 
every remaining element there will be a pair.
"""


"""
Below Mentioned approach is brute force approach, time complexity of the algorithm is O(N)

"""

def brute(arr):

    if len(arr)==1:
        return arr[0]
    
    for index in range(len(arr)):
        if index==0:
            if arr[index]!=arr[index+1]:
                return arr[index]
        
        if index == len(arr)-1:
            if arr[index]!=arr[index-1]:
                return arr[index]
            
        if arr[index]!=arr[index-1] and arr[index] !=arr[index+1]:
            return arr[index]
        
    return -1


single_element_brute = brute(arr1)


print(f"single element in the arr using brute force approach is: {single_element_brute}")




"""
Below mentioend approach is the most optimal approach using binary search

"""


def binary(arr):
    
    if len(arr)==1:
        return arr[0]

    if arr[0]!=arr[1]:
            return arr[0]

    if arr[len(arr)-1]!=arr[len(arr)-2]:
                return arr[len(arr)-1]
    
    low = 1
    high = len(arr)-2

    while low<=high:
        mid = (low+high)//2
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            return arr[mid]
         
        if ((mid%2==1) and arr[mid]==arr[mid-1]) or ((mid%2==0) and arr[mid]==arr[mid+1]):

            low = mid+1

        else:
             high = mid-1

    return -1

single_element_binary = binary(arr1)


print(f"single element using binary approach is : {single_element_binary}")