def countdown(num):
    new_list = []
    for x in range(num,0,-1):
        new_list.append(x)
    new_list.append(0)
    print(new_list)
countdown(5)

def print_and_return(list):
    print(list[0])
    return list[1]
print_and_return([0,1])

def first_plus_length(list):
    x = len(list)
    return list[0] + x
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    else:
        new_list2 = []
        for x in range(0,len(list),1):
            if list[x] > list[1]:
                new_list2.append(list[x])
        return new_list2
print(values_greater_than_second([5,2,3,2,1,4]))

def this_length_that_value(list):
    new_list3 = []
    for x in range(0,list[0],1):
        new_list3.append(list[1])
    return new_list3
print(this_length_that_value([4,7]))
print(this_length_that_value([6,2]))