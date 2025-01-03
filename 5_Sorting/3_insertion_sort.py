
arr = [1,4,3,2,6,8,9,7]



for i in range(len(arr)-1):
    j=i
    while j>0:
        if arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]

        j=j-1
    

print(f"sorted array using insertion sort is {arr}")
    