number = int(input("enter the number:"))

def factorial(n):

    if n==1:
        return 1
    return n*factorial(n-1)



print(factorial(5))