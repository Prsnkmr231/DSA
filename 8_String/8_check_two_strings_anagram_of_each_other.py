
"""
Leetcode Problem - 242 - https://leetcode.com/problems/valid-anagram/description/
"""


def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if sorted(s)==sorted(t):
        #     return True
        # return False

        s_dict = {}
        t_dict = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            s_dict[s[i]]=1+s_dict.get(s[i],0)
            t_dict[t[i]]=1+t_dict.get(t[i],0)
        if s_dict==t_dict:
            return True
        return False

s = "anagram", 
t = "nagaram"
anagram_checker = isAnagram(s,t)

