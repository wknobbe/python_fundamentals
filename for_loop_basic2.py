def biggie_size(list):
    for x in range(0,len(list),1):
        if list[x] > 0:
            list[x] = "big"
    return list
print(biggie_size([-1,3,5,-5]))

def count_positives(list):
    count = 0
    for x in range(0,len(list),1):
        if list[x] > 0:
            count += 1
    list[len(list)-1] = count
    return list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

def ultimate_analysis(list):
    sum = 0
    length = len(list)
    max = list[0]
    min = list[0]
    for x in range(0,length,1):
        sum += list[x]
        if list[x] > max:
            max = list[x]
        if list[x] < min:
            min = list[x]
    average = sum / length
    new_dict = {'Sum': sum, 'Average': average, 'Min': min, 'Max': max, 'Length': length}
    return new_dict
print(ultimate_analysis([37,2,1,-9]))

def reverse_list(list):
    for x in range(0,int(len(list)/2),1):
        temp = list[x]
        list[x] = list[len(list)-1-x]
        list[len(list)-1-x] = temp
    return list
print(reverse_list([37,2,1,-9]))
print(reverse_list([0,1,2,3,4,5,6,7,8,9,10]))