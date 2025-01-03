

string = input("Enter the string:")

length = len(string)
index = 0
def string_palindrome(index,string):


    if index>len(string)//2:
        return True
    
    if string[index]!=string[len(string)-index-1]:
        return False
    
    return string_palindrome(index+1,string)
       

if string_palindrome(index,string):
    print("given string is a palindrome")

else:
    print("given string is not a palindrome")