
"""
problem statement: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone 
and will come back in h hours.Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.Koko likes to eat slowly but still wants to 
finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours
"""



piles = [3,6,7,11]
h = 8


"""
Explanation: koko can choose any number of bananas to eat per one hour,it will choose  wisely so that the choosen number makes it
to eat all the bananas,there are number of numbers it can choose to eat all the bananas,but the number it choose should be small 
number

"""


"""
Below mentioned approach is linear search,it search for each and every element unitl the maximum pile of banana and finds out the
number of bananas per hour to eat.
"""
def total_hrs(piles,bananas_per_hr):
    tot_hrs =0
    for element in piles:
        quotient = element//bananas_per_hr
        remainder = element%bananas_per_hr
        if remainder==0:
            tot_hrs+=quotient
        else:
            tot_hrs+=quotient+1
    return tot_hrs


def brute(piles):
    i=1
    while i<=max(piles):
        if total_hrs(piles,i)<=h:
            return i
        i+=1
        
hrs = brute(piles)

print(f"number of hrs using brute is {hrs}")


def binry_srch(piles):
    low = 1
    high = max(piles)
    ans = float('inf')
    while low<=high:
        mid = (low+high)//2

        if total_hrs(piles,mid)<=h:
            high = mid-1
            ans = mid
        else:
            low = mid+1

    return low

hrs_binary = binry_srch(piles)

print(f"number of hrs taken using binary search is: {hrs_binary}")



