# find the lowest value in list

list = [1,27,5,8,2,0]
minValue = list[0]

for i in list:
  if i > minValue:
    i = minValue
    
print('Lowest Value is', minValue)