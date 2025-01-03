

arr = [13,16,11,9,27,14,7,4,5,10,1,2,19]

smallest = arr[0]
second_smallest = float('inf')

for element in arr:
    if element < smallest:
        second_smallest = smallest
        smallest = element

    elif element > smallest and element <second_smallest:
        second_smallest = element

print(f"second smallest element in the array is: {second_smallest}")



"""
Time complexity of the algorithm is O(n)
"""