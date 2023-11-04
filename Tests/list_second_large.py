def sec_large(list1):
    largest = list1[0]
    sec_largest = list1[0]
    for x in list1:
        if x > largest:
            sec_largest = largest
            largest = x
    return sec_largest

def find_second_largest(lst):
    if len(lst) < 2:
        return None  # Not enough elements to find the second-largest

    max_element = max(lst)
    lst.remove(max_element)  # Remove the first occurrence of the largest element
    second_largest = max(lst)

    return second_largest
        

list1 = [3, 1, 4, 4, 5, 2]
print(sec_large(list1))
print(find_second_largest(list1))