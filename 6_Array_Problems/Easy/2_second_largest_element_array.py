arr = [13,16,11,9,27,14,7,4,5,10,27,1,2,19]


#Brute Force Approach  using sorted function


sort_array = sorted(arr)
second_largest = sort_array[-2]

"""
Above approach only works if there are no duplicate values in the array.If the maximum element is present as duplicates then 
the approach does not work.you have to follow the below mentioned approach.
"""

j=len(sort_array)-2
while j>0:
    if sort_array[j]==sort_array[-1]:
        j = j-1
    else:
        break
second_largest = sort_array[j]

print(f"sort_array is {sort_array}")
print(f"second largest element in the array using brutal approach is :{second_largest}")


"""
In worst case the time complexity is O(nlogn + n)
"""

##better Approach 


largest = arr[0]

for element in arr:
    if element>largest:
        largest=element

slargest = -1

for element in arr:
    if element>slargest and element<largest:
        slargest = element


print(f"slargest element in the array using better approach  is: {slargest}")


"""
Time comlexity of the algorithm is O(2N).It is better than O(nlogn)
"""


##optimal approach 


largest = arr[0]
slargest_optiml = -1

for element in arr:
    if element > largest :
        slargest_optiml = largest
        largest = element
    elif element<largest and element>slargest_optiml:
        slargest_optiml = element


print(f"second largest element in tha array using optimal approach is:{slargest_optiml}")


"""
Time complexity of this algorithm is O(n)
"""
