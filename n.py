order = [1,48,2,4,6,8,13,12,18,20]
#for i in range(len(order) - 1):
    #min_index = i
    #for j in range( i + 1, len(order)):
        #current_item = order[j]
        #if current_item < order[min_index]:
            #min_index = j
    #order[i], order[min_index] = order[min_index], order[i]

for i in range(len(order) - 1):
    for j in range(0, len(order) - i - 1):
        if order[j] > order[j + 1]:
            order[j], order[j + 1] = order[j + 1], order[j]
print(order)