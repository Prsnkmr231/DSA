number = int(input("Enter the number:"))
checker = 2
flag = True
if number>1:
    while checker**2 <=number:

        if number%checker==0:

            flag=False
        checker+=1

print(f"flag is :{flag}")
if flag:
    print(f"Number is prime")