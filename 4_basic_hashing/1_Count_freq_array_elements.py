

array = [ 1,2,3,4,3,6,7,8,4,6,9,1,3,6,4,5]

freq_dict = {}

for element in array:
    if element not in freq_dict.keys():
        freq_dict[element]=1
    else:
        freq_dict[element]+=1

print(f"frequency of the elements in the array is {freq_dict}")