def sum_target(list1, target):
    new_list =[]
    for i in range(len(list1)):
        new_list.extend([(list1[i], y) for y in list1[i:] if list1[i]+y == target])
    print(new_list)


def find_pairs_with_sum(lst, target_sum):
    # Create a dictionary to store elements and their indices.
    element_indices = {}
    pairs = []

    for index, num in enumerate(lst):
        complement = target_sum - num

        # Check if the complement of the current element exists in the dictionary.
        if complement in element_indices:
            pairs.append((complement, num))

        # Add the current element to the dictionary.
        element_indices[num] = index

    return pairs

list1 = [1, 2, 3, 4, 5]
target = 7
sum_target(list1, target)

result = find_pairs_with_sum(list1, target)
print("Pairs with sum", target, "are:", result)