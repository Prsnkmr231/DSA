

arr = [0,1,0,2,2,1,1,0,0,0,2,2,1,1]

#Brute Force Approach using inbuilt sorted function in python

brute_sorted = sorted(arr)
print(f'sorted array of 0"s 1"s and 2"s using brute_force_approach is  {brute_sorted}')


"""
Time Complexity of the algorithm is O(nlogn) because time complexity of any sorted algorithm is nlogn
"""

#better approach is using three variables to store the count of the number of 0's and 1's and 2's


counter_0 =0
counter_1 =0
counter_2 = 0

for element in arr:
    if element==0:
        counter_0+=1
    if element==1:
        counter_1+=1
    if element==2:
        counter_2+=1

for index in range(counter_0):
    arr[index] = 0

for index in range(counter_0,counter_0+counter_1):
    arr[index] = 1

for index in range(counter_0+counter_1 , counter_0+counter_1+counter_2):
    arr[index] =2

print(f"counter_0,counter_1,counter_2 are {counter_0,counter_1,counter_2}")

print(f'sorted array using better approach is {arr}')

"""
Time complexity of the  above algorithm is O(2n),because there are two for loops running for n number of elements.

"""


#optimal approach is using dutch national flag algorithm 


"""
Dutch National flag algorithm intuition

[0---low-1] = 0
[low --- mid-1] =1
[high+1 ----- n-1] =2 



These algorithm follows the below mentioned  assumptions that the 

[0 ----low-1]  - In this array the mentioned slice contains the sorted zeros
[low-----mid-1] - In this array the mentioned slice contains the sorted ones
[mid------high] - In this array the mentioned slice contains the unsorted values
[high+1 ----- n-1] - In this array the mentioned slice contains the sorted twos



we are going to assign the values as mentioned below

low = 0
mid = 0
high = n-1  by taking these values the above assumtions are satisfied.


after that we are going to check the condition until mid <=high  in the while loop

if  the arr[mid]==0, swap the values of arr[mid],arr[low]
    increment the mid value by 1 and increment the low value by 1.
if the arr[mid] == 1, increment the mid value by 1 
if the arr[mid] ==2, swap the value of arr[mid],arr[high],
    decrement the high value by 1



"""



arr1 = [0,1,0,2,2,1,1,0,0,0,2,2,1,1]

low = 0
mid = 0
high = len(arr1)-1
count = 1
while mid<=high:
    count=count+1
    print(count)
    print(f"low value is {low}")
    print(f"mid value is {mid}")
    print(f"high value is {high}")
    if arr1[mid]==0:
        print(f"executing in if loop")
        arr1[low],arr1[mid]=arr1[mid],arr1[low]
        mid = mid+1
        low = low+1
    elif arr1[mid]==1:
        print(f"executing in elif loop")
        mid = mid+1

    elif arr1[mid]==2:
        print(f"executing in else loop")
        arr1[high],arr1[mid]=arr1[mid],arr1[high]
        high = high-1

print(arr1)


"""
Time Complexity of the above algorithm is O(N)
"""


