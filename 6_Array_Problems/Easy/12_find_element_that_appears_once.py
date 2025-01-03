
arr = [1,1,2,2,3,3,4,5,5]


#Brute Force Approach 
number = 5
def find_element_appears_once(arr,number):
    for i in range(5):
        counter = 0
        for j in range(len(arr)):
            if i==arr[j]:
                counter+=1

        if counter==1:
            return i
        
element = find_element_appears_once(arr,number)
print(f"element that appears only once is: {element}")


"""
Time Complexity of the above algorithm is O(m*n)  where m is the number and n is the length of the array.

"""


#better approach using hashtables.

def find_element_that_appears_once_hash(arr,number):
    freq_dict = {}
    for i in arr:
        freq_dict[i] = freq_dict.setdefault(i,0)+1
    
    for key,value in freq_dict.items():
        if value<2:
            return key


print(f"element that appears only once usign hashtables are : {find_element_that_appears_once_hash(arr,number)}")


"""
Time complexity of the above algorithm is O(n)+O(m) n is the number of elements in the array and m is the number of unique keys in the 
dictionary
"""



#optimal approach using xor operation

def find_element_that_appears_once_xor(arr):
    xor = 0
    for element in arr:
        xor = xor^element
    return xor

print(f"element that appears only once using xor operation is : {find_element_that_appears_once_xor(arr)}")


"""
Time Complexity of the above algorithm is O(n) and space complexity is o(1)
"""