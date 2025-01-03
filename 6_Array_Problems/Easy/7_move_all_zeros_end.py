arr = [1,0,2,3,0,0,4,5,0,0,6,0,7]

##Brute force approach for moving zeroes to the end;


"""
In the below algorithm it finds out the non zero elements and store the elements in the temp list.And once all the non zero elements
are stored in the temp.Then we iterate a for loop for the difference between the arr length and temp length.we are going to append that 
many number of zeroes to the temp list.

Time complexity of the above algorithm is O(n),it iterates through the entire array  and Space complexity of the above algorithm is 
O(n) because it is going to store the number of elements equal to arr
"""

temp = []

def brutal(arr,temp)
    for i in arr:
        if i!=0:
            temp.append(i)
    for j in range(len(arr)-len(temp)):
        temp.append(0)

    return temp

brute_zeros_end_array = brutal(arr,temp)


"""
In the below algorithm we are using two pointer approach.we will iterate through the array and find out the non zero element,whenever we 
find out the non zero element we are going to replace the value with the element at index j and update the pointer j to j+1 and in this 
way we are going to move the zeros to end.


Time complexity of the algorithm is O(n) and space complexity of the algorithm is O(1)

"""

def move_zeros_end(arr):
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j = j+1

    return arr
    

zeroes_end_array = move_zeros_end(arr,j=0)

print(f"Zeroes end array is {zeroes_end_array}")


    


