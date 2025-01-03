arr = [2,3,2,2,7,2,7,2,2,3,3,1,2,2]

#Problem Statement - Find the majority element greater than half the length of the array


#Brute Force Approach

def majority_element_brute(arr):
    for i in range(len(arr)):
        counter = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                counter+=1

        if counter>len(arr)//2:
            return arr[i]
    return "No Majority element found"

print(f"majority element is : {majority_element_brute(arr)}")



#Better Approach using hashmaps


def majority_element_better(arr):
    hash_map = {}
    for i in arr:
        hash_map[i]= hash_map.setdefault(i,0)+1

    for key,value in hash_map.items():
        if value>(len(arr)//2):
            return key
        
    return "No Majority Element Found"


print(f"majority element is {majority_element_better(arr)}")



"""
Time Complexity of the above algorithm is O(N)+O(N) = O(2N) and space complexity of the above algorithm is O(N) it is going to store
N distinct keys.

"""


#optimal approach using moores voting algorithm


def majority_element_optimal(arr):
    counter = 0
    element = 0

    for i in range(len(arr)):
        if counter==0:
            counter+=1
            element = arr[i]
        if element==arr[i]:
            counter+=1
        
        if element!=arr[i]:
            counter-=1

    counter1 =0

    for i in range(len(arr)):

        if element == arr[i]:
            counter1+=1
    
    if counter1>len(arr)//2:
        return f"Majority element using optimal approach is {element}"
    


print(majority_element_optimal(arr))



