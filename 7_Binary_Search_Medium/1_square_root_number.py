
number = 28

"""
Problem statement:
    Find the sqaure root of the element,if the number has a float value as a sqaure root.find the floor value of that number.


"""


"""
Below mentioned approach is brute force approach,where we can use the linear search for finding the sqaure root of the number.
Time complexity of the algorithm is O(sqrt(N)) == O(N)
"""

def brute_sqrt(number):
    value =1
    ans = 0
    while value*value<=number:
        ans=value
        value+=1
    return ans

sqrt_brute = brute_sqrt(number)

print(f" the sqaure root of the number using brute force approach is: {sqrt_brute}")



"""
Below mentioned approach is using optimal binary search,it uses binary search algorithm to find the square root of that number.
Time complexity of the algorithm is o(log2(n))
"""



def binary_sqrt(number):
    low=1
    high = number
    ans = 0
    while low<=high:
        mid = (low+high)//2
        if mid*mid<=number:
            ans = mid
            low= mid+1
        else:
            high = mid-1
    return ans

sqrt_binary = binary_sqrt(number)

print(f"square root of the number using binary search is {sqrt_binary}")
        