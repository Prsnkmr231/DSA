arr = [1,2,3,4,5,6,7,8]

arr1 = arr
d_places = int(input("Enter the times you want to rotate the array:"))


# Rotating the array right by d places using slicing 

d_places = d_places % len(arr)
arr = arr[-d_places:] + arr[:-d_places]
print(f"left rotated array by d times is {arr}")


"""
Time complexity of the above algorithm is O(n) and the space complexity of the algorithm is O(n), to redcue the space complexity to 
O(1) use the below mentioned optimal approach.

"""



"""
Algorithm 

1.Reverse the entire array from 0 to length(n-1)
2.Reverse the array from 0 to d_places-1
3.Reverse  the array from d_places to len(arr)-1

"""

def custom_reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start+1
        end = end-1


def rotate_left(arr,d_places):
    print(f'array is {arr}')
    custom_reverse(arr,0,len(arr)-1)
    custom_reverse(arr,0,d_places-1)
    custom_reverse(arr,d_places,len(arr)-1)



"""
Time complexity of the above algorithm is O(n) and space complexity of the algorithm is O(1)

"""
    