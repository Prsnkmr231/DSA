"""
Leetcode - 451 - https://leetcode.com/problems/sort-characters-by-frequency/description/

"""


def frequencySort(s: str) -> str:
        count_frequency = {}
        for char in s:
            count_frequency[char] =1+count_frequency.get(char,0)
        string =  ""
        sorted_dict = sorted(count_frequency.items() ,key=lambda item : item[1],reverse=True)
        for value in sorted_dict:
            string+=value[0]*value[1]
        return  string

s=  "cccaaa"
sort_str_frequency = frequencySort(s)

print(f"sorted string using frequency is : {sort_str_frequency}")