number = int(input("Enter the number :"))
number2 = number



#Approach-1

digits_lst= []
while number>0:
   digit = number%10
   number = number//10
   digits_lst.append(digit)

print(f"count of digits are:{len(digits_lst)}")
print(f"digits are:{digits_lst}")




#Approach-2
import math
count= int(math.log10(number2)+1)
print(f"\n\ncount of the digits using second appraoch are :{count}")