"""
Leet code Problem -151 - https://leetcode.com/problems/reverse-words-in-a-string/


"""

def reverseWords(s):
        return  " ".join(s.strip().split()[::-1])


s = "a good   example"
output = reverseWords(s)

print(f"output from the function is : {output}")

# print(output)


"""
If you use .split() operator with inverted commas as a argument in that case it splits multispace character into that number of splits.So try to use
the default one without any arguments to the split() operator.

"""

