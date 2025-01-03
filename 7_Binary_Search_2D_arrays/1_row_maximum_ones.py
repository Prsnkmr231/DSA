arr =  [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]




"""
Problem Statement: find out the row with maximum number of ones, if there are multiple rows with maximum number of ones 
then you have to give the smallest index with the maximum number of ones.
"""


"""
Below Approach is the brute force approach, it iterates through each row , and in that row it iterates through each and 
every element and checks 1 is present or not. Time Complexity of the algorithm is O(M*log2N)

"""

def Brute_Force(arr,target):
    max_ones_counter = 0
    index = -1
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            if arr[row][column]==1:
                ones_counter = len(arr[row])-column
                if ones_counter>max_ones_counter:
                    max_ones_counter = ones_counter
                    index= row
                break
        
    return max_ones_counter,index 

brute_ones,brute_index = Brute_Force(arr,1)   



print(f"brute_ones and brute_index are: {brute_ones,brute_index}")




"""
Below Approach is the optimal approach, it iterates through each and every array then it applies the binary search so that the time complexity of the algorithm 
is O(n*log2M)
"""


def Binary_Search(arr_1,target):
        
        low = 0
        high = len(arr_1)-1
        ans = len(arr_1)
        while low<=high:
            mid = (low+high)//2
            if arr_1[mid]>=target:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans

def rowWithMax1s(arr):
        
        max_ones_counter=0
        row_index = -1
        
        for index in range(len(arr)):
            
            ones_counter = len(arr[index])-Binary_Search(arr[index],1)
            if ones_counter>max_ones_counter:
                max_ones_counter = ones_counter
                row_index = index
                
        return row_index


max_ones_index = rowWithMax1s(arr)

print(f"max_ones_index using optimal approach is  : {max_ones_index}")