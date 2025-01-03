

number = int(input("enter the number:"))

def func_n_1(number):

    if number>0:
        print(f"number is {number}")
    else:
        return
    number = number-1
    return func_n_1(number)

func_n_1(number)