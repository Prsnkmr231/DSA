

number = int(input("enter the number:"))

def func_1_n(num):

    if num<=number:
        print(f"num is : {num}")
    else:
        return 
    num+=1
    return func_1_n(num)

func_1_n(1)