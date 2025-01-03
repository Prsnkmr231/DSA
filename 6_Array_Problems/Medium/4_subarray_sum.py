
arr = [-2,-3,4,-1,-2,1,5,-3]

max = 0

def subarray_sum_brutal(arr):
    for i in range(len(arr)):

        for j in range(i,len(arr)):
            sum =0
            for k in range(i,j):
                sum+=k
            if sum>max:
                max = sum