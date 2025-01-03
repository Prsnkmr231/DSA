
a = [2,4,6,8,8,8,11,13]


"""
Problem Statement- 

Find out the index of the  first occurance of the target element  and the index of the last occurance of the target element

"""

"""
The first approach is the brute force approach using linear search and some comditions,time complexity of the algorithm is  O(n)

"""

def first_last_brute(a,target):
    first = -1
    last = -1
    for index in range(len(a)):
        if a[index]==target:
            if first==-1:
                first=index
                last = index
            else:
                last = index

    return first,last


first,last = first_last_brute(a,15)   


print(f"first and last occurence of the target element are: {first,last}")



"""
The second approach is using the  binary search and some conditions,time complexity of the algorithm is O(log2N)

"""


def first_last_binary(a,target):
    l_low = 0
    l_high = len(a)-1
    l_ans = len(a)-1
    while l_low<=l_high:
        l_mid = (l_low+l_high)//2

        if a[l_mid]>=target:
            l_ans = l_mid
            l_high = l_mid -1
        else:
            l_low = l_mid+1

    
    h_low = 0
    h_high = len(a)-1
    h_ans = len(a)-1

    while h_low<=h_high:
        h_mid = (h_low+h_high)//2

        if a[h_mid]>target:
            h_ans = h_mid
            h_high = h_mid -1
        else:
            h_low = h_mid+1

    if (l_ans==len(a)) | a[l_ans]!= target:
        l_ans = -1
        h_ans = -1
    else:
        h_ans = h_ans-1

    return l_ans,h_ans

first_bin,last_bin = first_last_binary(a,12)

print(f"first and last occurance using binary is {first_bin,last_bin}")


