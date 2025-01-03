"""

leetcode problem - 1614 - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

"""

def maxDepth(s: str) -> int:
        lst = []
        maximum = 0
        for char in s:
            if char =="(":
                lst.append(char)
                if maximum<=len(lst):
                    maximum=len(lst)
            elif lst and char==")":
                lst.pop()
        return maximum



s = "(1+(2*3)+((8)/4))+1"
value = maxDepth(s)

print(f"maximum depth of the string is : {value}")