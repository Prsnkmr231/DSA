num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


while num1>0 and num2>0:
    if num1>num2:
        num1 = num1%num2

    else: 
        num2 = num2%num1

if num1==0:
    print(f"gcd or hcf is:{num2}")
else:
    print(f"gcd or hcf is : {num1}")