
arr = [1,2,4,5]

def missing_element(arr,n):
    for element in range(1,n):
        if arr[element-1]!=element:
            return element
        

mis_element = missing_element(arr,5)

print(f"missing element in the array is: {mis_element}")



"""
Time Complexity of the above algorithm is O(n) and space complexity of the algorithm is O(1)

"""