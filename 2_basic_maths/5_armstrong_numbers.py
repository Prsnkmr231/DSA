

number = int(input("Enter the number:"))

temp = number
sum = 0

while number>0:
    sum+= (number%10)**3
    number = number//10

if sum==temp:
    print("number is a armstrong number")
else:
    print("number is not a armstrong number")