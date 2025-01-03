
arr = [13,16,11,9,27,14,7,4,5,10,1,2,19]



##BRUTE FORCE APPROACH using inbuilt functions like sorted

sort_array = sorted(arr)
largest_element = sort_array[-1]
print(f"largest element using sorted function is:{largest_element}")

"""
time complexity of the above algorithm is O(nlogn)
"""


##Brute Force Approach-2 using inbuilt function like max

max_element = max(sort_array)
print(f"maximum element using max function is :{max_element}")


"""
time complexity of the above algorithm is O(n) it works in the same fashion as optimal approach mentioned below.
"""





largest = arr[0]

for element in arr:
    if element>largest:
        largest = element

print(f"largest element in the array is:{largest}")

"""
time complexity of the algorithm is O(n)
"""