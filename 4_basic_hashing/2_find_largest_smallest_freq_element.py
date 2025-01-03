array = [ 1,2,3,4,3,6,7,8,4,6,9,1,3,6,4,5]

freq_dict = {}

for element in array:
    if element not in freq_dict.keys():
        freq_dict[element]=1
    else:
        freq_dict[element]+=1
sorted_items = sorted(freq_dict.items(),key=lambda item : item[1],reverse=True)

print(sorted_items)