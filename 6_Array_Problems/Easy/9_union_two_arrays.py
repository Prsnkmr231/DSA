arr1 = [1,1,2,3,4,4,5,6,6]
arr2 = [3,4,4,5,6,7,7,8,8,9]


union1 = list(set(arr1))

for element in arr2:
    if element not in union1:
        union1.append(element)


print(f"union of the two arrays using set and for loop is:{union1}")



union2 = set(arr1).union(set(arr2))
print(f"union of the two arrays using union function between sets are : {union2}")



arr1.extend(arr2)
union3 = set(arr1)
print(f"union of the array by extending an array and using set function is {union3}")





