list1 = [1,2,3,4,5,2]
list2 = [9,8,[]]

list2.extend(list1)
print(list2)
print(list1)

for item in list2:
    if isinstance(item, list):
        for thing in list1:
            item.append(thing)

print("after merge: ", list2)

list2.insert(2,23)

print("after insert: ", list2)

list2.remove(23)

print("after remove: ", list2)

print("poping: ",list2.pop(2))
print("index: ",list2.index(2))
print("index2: ",list2.index(2, 5))
print(list2.count(2))