

arr = [2,6,5,8,11]


target = 14

#Brute Force Approach

def find_two_sum_brutal(arr,target):

    for element in range(len(arr)):
        print(arr[element])
        for j in range(element+1,len(arr)):
            print(arr[j])
            if arr[element]+arr[j]==target:
                return f"yes target sum found at index {element}: {arr[element]} and {j}:{arr[j]}"
    
    return "NO target sum not found"
        

print(f"{find_two_sum_brutal(arr,target)}")

"""
in worst case the time complexity of this algorithm is O(n^2).
the space complexity of the algorithm is O(1)

"""


#Better approach using hash arrays 


def find_two_sum_better(arr,target):
    hash_map = {}

    for index in range(len(arr)):
         required = target-arr[index]
         if required in hash_map:
             return f"element at {index} index:{arr[index]}, required element at {hash_map[required]} index is : {required}"
         else:
             hash_map[arr[index]] = index
    return "sum of two elements that gives the target is not found"


print(f"{find_two_sum_better(arr,target)}")


