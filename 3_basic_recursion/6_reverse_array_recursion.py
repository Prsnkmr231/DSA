

arr = [1,2,3,4,5]

index = 0
length = len(arr)
def reverse_array(index,arr):

    if index<length//2:

        arr[index],arr[length-index-1] = arr[length-index-1],arr[index]
        return reverse_array(index+1,arr)
reverse_array(index,arr)


