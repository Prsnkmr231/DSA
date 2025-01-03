

number = int(input("enter the number : "))

temp_number = number

#Approach -1

reverse_num =0
while number > 0:
    digit = number%10
    reverse_num = reverse_num*10+digit
    number = number//10

print(f"reversed number is : {reverse_num}")



#Approach -2

number_string = str(temp_number)
reversed_num = number_string[::-1]
print(f"reversed number using second appraoch is : {reversed_num}")



if int(reversed_num) == temp_number:
    print(f"number is a palindrome checked using the string approach")


if reverse_num == temp_number:
    print(f"number is a palindrome")

else:
    print(f"Number is not a palindrome")