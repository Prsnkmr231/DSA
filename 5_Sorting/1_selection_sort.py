

"""
Selection sort:

iteration - 1 i=0

its assume that the ith index(i=0) contains the minimum element and stored in the min_index variable.
Then by using a for loop check the whole array (from i=0 to n-1) that is there any other index that contains the minimum element.
if any index contains then the min_index variable is updated to that index.
once we find out the minimum index, then we will swap the ith element with the minimum index element.


iteration - 2  i=1

In the second iteration also, we are going to assume the minimum index element is present at ith index(i=1) and stored in the min-index 
variable.Then by using a for loop check the array (from i=1 to n-1) that there is any other index contains the minimum element.if 
contians we are going to update the min_index variable with that index.then we will the ith element with the minimum index element.

this process is continued until the ith element reaches i=len(arr)-2



time complexity of the selection sort algorithm is o(n2)

"""



arr = [1,4,3,2,6,8,9,7]


for i in range(len(arr)-2):
    min_index = i
    for j in range(i,len(arr)-1):
        if arr[min_index]>arr[j]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]

print(f"sorted array using selection sort is:{arr}")