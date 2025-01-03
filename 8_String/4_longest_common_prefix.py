"""
Leet Code Problem - 14 - https://leetcode.com/problems/longest-common-prefix/description/

"""

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs)==0:
            return ""

        if len(strs)==1:
           return strs[0]

        if len(strs)>1:
            start_string = strs[0]
            for index in range(len(start_string)):
                char = start_string[index]
                for string in strs[1:]:

                    if index>=len(string) or string[index]!=char:
                        return string[:index]
                
                else:
                    return start_string

        return ""