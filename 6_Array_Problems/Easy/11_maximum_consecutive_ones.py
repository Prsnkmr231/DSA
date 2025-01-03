

arr = [1,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1]

counter = 0
maximum = 0
for element in arr:
    if element==1:
        counter+=1
        maximum = max(counter,maximum)
    else:
        counter =0


print(f"maximum number of consecutive ones is {maximum}")