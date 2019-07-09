n_int = [1,5,3,-2,2,-3,-5,6,-1]
#plus_int , minus_int = [] , []
sorted_numbers = []
i = 0

for sort in n_int:
    if sort > 0:
        sorted_numbers.insert(i,sort)
#        plus_int.append(sort)
        i += 1
    else:
        sorted_numbers.append(sort)
#        minus_int.append(sort)

#result = plus_int + minus_int
#print(result)
print(sorted_numbers)