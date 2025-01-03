"""

Leetcode Problem - 796 https://leetcode.com/problems/rotate-string/description/
"""

def rotateString(s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for index in range(len(s)):
            if s==(goal[index:]+goal[0:index]):
                return True
        return False



s = "abcde" 
goal = "abced"

answer = rotateString(s,goal)