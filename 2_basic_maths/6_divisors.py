

number = int(input("enter the number:"))

checker = 1
divisors = []
while checker**2 <= number:
    if number%checker==0:
        divisors.append(checker)
        if checker!= number//checker:
            divisors.append(number//checker)
    checker+=1

print(f"divisors od the number are : {divisors}")
