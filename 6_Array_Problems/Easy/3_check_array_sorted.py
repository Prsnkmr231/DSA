

# arr = [1,2,3,4,5,6,7,8]
arr = [1,3,4,2,6,5,8,7]

flag = True
for i in range(len(arr)-2):
    if arr[i]>arr[i+1]:
        flag = False

if flag:
    print("array is sorted")

else:
    print("array is not sorted")