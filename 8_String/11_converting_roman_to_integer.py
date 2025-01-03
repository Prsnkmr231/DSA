"""
Leetcode Problem - 13 - https://leetcode.com/problems/roman-to-integer/description/
"""


"""
logic : convert each roman value into integer based on the hash table and store them into a list and then check that the next value is larger than 
the present value then assign negetive value to that.Add all the elemnts of the list.



"""

def brute_romanToInt(s: str) -> int:

        values_dict ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        lst = []

        for char in s:
            lst.append(values_dict[char])

        for index in range(len(lst)-1):
            if lst[index]>=lst[index+1]:
                continue
            else:
                lst[index]=-lst[index]
        return sum(lst) 

def optimal_romanToInt(s: str) -> int:
        
        values_dict ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        for index in range(len(s)-1):

            if values_dict[s[index]]>=values_dict[s[index+1]]:
                 sum+=values_dict[s[index]]
            else:
                 sum-=values_dict[s[index]]
        sum+= values_dict[s[-1]]
        return sum

s = "MCMXCIV"


brute_value = brute_romanToInt(s)

print(f'brute value is:{brute_value}')
optimal_vlaue = optimal_romanToInt(s)

print(f"optimal value is: {optimal_vlaue}")
