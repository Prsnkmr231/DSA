def removeOuterParentheses(s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        lst = []
        for char in s:
            if char=="(":
                lst.append(char)
                if len(lst)>1:
                    string = string+char
            if char==")":
                if len(lst)>1:
                    string=string+char
                    lst.pop()
                elif len(lst)==1:
                    lst.pop()
        return string
s ="(()())(())"
removeOuterParentheses(s)

print(f"executing")