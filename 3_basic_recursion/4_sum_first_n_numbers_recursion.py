

number = int(input("enter the number:"))

sum = 0

def sum_numbers_recursion(sum,number):

    if number<=0:
        return sum
    else:
        sum+=number
        number=number-1
    return sum_numbers_recursion(sum,number)


sum_numbers = sum_numbers_recursion(sum,number)
print(sum_numbers)