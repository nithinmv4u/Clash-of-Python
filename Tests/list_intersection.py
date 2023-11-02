def intersection(list1, list2):
    intersection_list = []
    for item in list1:
        if item in list2:
            intersection_list.append(item)
    return intersection_list

def intersection_fn(list1, list2):
    return list(set(list1) & set(list2))


list1= [1, 2, 3]
list2= [2, 3, 4]
# list1 = list(map(int,input("Enter list: ").strip().split()))
# list2 = list(map(int,input("Enter list: ").strip().split()))
result = intersection(list1, list2)
print(result)

result = intersection_fn(list1, list2)
print(result)