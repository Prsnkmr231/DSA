"""
leetcode Problem = 
"""


def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        brackets_dict = {")":"(","]":"[","}":"{"}

        for char in s:
            if char=="(" or char=="[" or char=="{":
                lst.append(char)
            elif char==")" or char=="]" or char=="}":
                    if lst and lst[-1]==brackets_dict[char]:
                        lst.pop()
                    else:
                        return False
        if len(lst)==0:
            return True
        else:
            return False
        

s = "([])"

test_bool = isValid(s)