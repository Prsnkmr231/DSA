
"""
Leetcode Problem - 8 - https://leetcode.com/problems/string-to-integer-atoi/

"""

def myAtoi(s: str) -> int:
        string = ""
        s = s.strip()
        digit_exists=False
        sign_exists = False
        if len(s)==0:
            return 0

        for char in s:
            if not char.isdigit() and char!="-" and digit_exists:
                if int(string) < -(2**31):
                    return -(2**31)
                elif int(string)>(2**31-1):
                    return (2**31)-1
                else:
                    return int(string)
            
            elif not char.isdigit() and char!="-" and char!="+" and not digit_exists:
                return 0
            elif not char.isdigit() and char=="-" and digit_exists:
                 return int(string)
            elif not char.isdigit() and (char=="-" or char=="+")  and not sign_exists:
                string = string+char
                sign_exists = True
                print("sign exists executed")
            elif not char.isdigit() and (char=="-" or char=="+") and sign_exists:
                print("executing")
                return 0
            elif char.isdigit():
                string= string+char
                digit_exists=True
        if string=="-" or not digit_exists:
            return 0
        
        print(f"string is: {string}")
        if int(string) < -(2**31):
            print("executing in minus condition")
            return -(2**31)
        elif int(string)>(2**31-1):
            return (2**31)-1
        return int(string)

s = "0-1"

s ="+-12"

s = "      -11919730356x"

value = myAtoi(s)

print(value)