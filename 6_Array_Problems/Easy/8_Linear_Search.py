arr = [1,4,6,2,7,3,9,5,8]


element = int(input("Enter the number you want to find :"))

def linear_search(arr,element):
    for i in range(len(arr)):
        if arr[i]==element:
            return i
    
    return -1
        

index = linear_search(arr,element)

print(f"index of the element is :{index}")