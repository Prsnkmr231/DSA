
number = 64

"""
Problem Statement: find the nth root of the number,if it exists return the value else return -1

"""


"""
Below mentioned approach is the linear search approach,time complexity of the algorithm is O(nth toot of that number)==O(N)
"""

# def sqr(index,times):
#     result =1
#     for val in range(1,times):
#         result+=result*index
#     return result


def brute_nthroot(number,times):
    for index in range(1,number):
        if index**times==number:
            return index
        if index**times>number:
            return -1
        
nthroot =  brute_nthroot(number,4)


print(f"the  nth root of the number is {nthroot}")


def binary_nthroot(number,times):

    low = 1
    high = number
    while low<=high:
        mid = (low+high)//2
        if mid**times==number:
            return mid
        
        if mid**times<number:
            low = mid+1
        else:
            high = mid-1

    return -1

nthroot_binary = binary_nthroot(number,4)
        
print(f"nth root of the number using binary search is {nthroot_binary}")