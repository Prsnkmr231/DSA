
arr = [2,4,6,8,8,8,11,13]

"""
Problem Statement:

Find the number of occurances of a target number in a sorted array:
"""


"""
Below Mentioned approach is brute force approach, it searches for a element using linear search found the number of occurances.
time complexity of the lagorithm is O(N)
"""

def count_num_occurances_brute(arr,target):
    count=0
    for element in range(len(arr)):
        if arr[element]==target:
            count+=1

    return count
target = 8
occur_brute = count_num_occurances_brute(arr,target)

print(f"number of occurances of element {target} is {occur_brute}")



"""
Below Mentioned approach is using lower bound and upper bound in binary search.time complexity of the algorithm is 2*O(log2N)

Lower Bound : finds out the smallest index of the  element that is greater than or equal to the target
Upper Bound : finds out the smallest index of the element that is greater than the target

1.once we found the lower bound and upper bound 
2.check the condition that lower bound and upper bound is not equal to -1
3.then find out the difference between upper bound and lower bound and add 1


"""



def count_num_occur_binary(arr,target):
        l_low = 0
        l_high = len(arr)-1
        l_ans = len(arr)
        while l_low<=l_high:
            l_mid = (l_low+l_high)//2

            if arr[l_mid]>=target:
                l_ans = l_mid
                l_high = l_mid -1
            else:
                l_low = l_mid+1

        
        h_low = 0
        h_high = len(arr)-1
        h_ans = len(arr)

        while h_low<=h_high:
            h_mid = (h_low+h_high)//2

            if arr[h_mid]>target:
                h_ans = h_mid
                h_high = h_mid -1
            else:
                h_low = h_mid+1

        if len(arr)>0 :
            if l_ans==len(arr):
                l_ans = -1
                h_ans = -1
            else:
                if (arr[l_ans]!= target):
                    l_ans = -1
                    h_ans = -1
                if l_ans!=h_ans:
                    h_ans = h_ans-1
        else:
            l_ans = -1
            h_ans = -1
            
        
        if l_ans!=-1 and h_ans!=-1:
           return (h_ans-l_ans)+1
        else:
            return 0
        
occur_binary =  count_num_occur_binary(arr,8)

print(f"occur_binary is: {occur_binary}")