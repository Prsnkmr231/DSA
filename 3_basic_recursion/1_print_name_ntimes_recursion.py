
times = int(input("enter the number of times you want to print the name : "))


def name_printer(times):
    if times>0:
       print("prasanna kumar")
    else:
        return 
    times=times-1
    return name_printer(times)


name_printer(times)