arr = [1,2,3,4,5,6,7,8]

arr1 = arr


d_places = int(input("Enter the times you want to rotate the array:"))

# Rotating the array left by d places using slicing 

d_places = d_places % len(arr)
arr = arr[d_places:] + arr[:d_places]
print(f"left rotated array by d times is {arr}")



"""
Time complexity of the above algorithm using slicing is O(n) and it takes the space complexity of O(n),If you want to reduce the space 
complexity to O(1) you can use the following below mentioned optimal approach.
"""


#Rotating the array left by d places using reverse function.

"""
Algorithm 

1.Reverse the slice of the array from 0 to d_places-1
2.Reverse the slice of the array from d_places to len(arr)-1
3.Reverse the slice of the array from 0 to len(arr)-1



"""



def custom_reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start+1
        end = end-1


def rotate_left(arr,d_places):
    print(f'array is {arr}')
    custom_reverse(arr,0,d_places-1)
    custom_reverse(arr,d_places,len(arr)-1)
    custom_reverse(arr,0,len(arr)-1)


rotate_left(arr,d_places)
print(f'array is {arr}')











