

"""

Leetcode Problem - 205  https://leetcode.com/problems/isomorphic-strings/

"""

"""
Below Mentioned Approach is the brute force approach

"""
def isIsomorphic_brute(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==1 and len(t)==1:
            return True
        str_dict = {}
        if len(s)==len(t):
            for index in range(len(s)):
                if s[index] not in str_dict.keys() and  t[index] in str_dict.values():
                        return False
                elif s[index] not in str_dict.keys():
                    str_dict[s[index]]=t[index]

                else:
                    if str_dict[s[index]]!=t[index]:
                        return False
            return True
        else:
            return False
        

"""
Below mentioned approach is the optimal approach

"""

def isIsomorphic_optimal(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.index(c) for c in s]==[t.index(c) for c in t]



s="paper"
t="title"


brute_bool = isIsomorphic_brute(s,t)
optimal_bool = isIsomorphic_optimal(s,t)


