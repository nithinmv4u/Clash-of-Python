def rotate_right(list1, num_position):
    num_position %= len(list1)
    return list1[num_position+1:]+list1[:num_position+1]

list1 = [1, 2, 3, 4, 5]
num_position = 7
result = rotate_right(list1, num_position)
print(result)