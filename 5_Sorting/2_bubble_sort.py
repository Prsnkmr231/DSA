
"""
Bubble sort


it works by push the maximum element using adjacent swappings.

iteration-1 i=0

In the inner loop it checks the jth index value and j+1th index value, if jth index value is greater than j+1th index value.Then it
swaps the jth index and j+1th index elements.

for every iteration the same operation is performed.

worst time complexity of the algorithm is o(n2)

best time complexity of the algorithm is o(n)

"""

arr = [1,4,3,2,6,8,9,7]

for i in range(len(arr)-2):
    for j in range(0,len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]


print(arr)
