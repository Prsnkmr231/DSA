


arr = [13,16,11,9,27,14,7,4,5,10,1,2,19]

smallest = arr[0]

for element in arr:
    if element<smallest:
        smallest = element

print(f"smallest element in the array using optimal apparoach is:{smallest}")