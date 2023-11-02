def occuarance(list1, num):
    while num in list1:
        list1.remove(num)
    return list1

def remove_element(list1, num):
    return [x for x in list1 if x != num]    

list1 = [1, 2, 2, 3, 4, 2]
num = 2

result = occuarance(list1, num)
print(result)

list1 = [1, 2, 2, 3, 4, 2]
num = 2

result = remove_element(list1, num)
print(result)