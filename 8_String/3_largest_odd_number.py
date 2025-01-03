"""
leetcode problem -1903 - https://leetcode.com/problems/largest-odd-number-in-string/

"""


def largestOddNumber(num):
        number = int(num)
        while number>0:
            if number%2!=0:
                return str(number)
            else:
                number = number/10

        return ""

num = "35427"

value = largestOddNumber(num)
if len(value)>0:
     print(f"largest odd number is : {value}")

else:
    print("there are no largest odd number")