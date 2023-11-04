def sort_length(fruits):
    fruits.sort(key=lambda x : len(x))
    return fruits

def sort_strings_by_length(strings):
    return sorted(strings, key=len)

fruits = ["apple", "banana", "cherry", "date"]
print(sort_length(fruits))

result = sort_strings_by_length(fruits)
print("Sorted by length:", result)