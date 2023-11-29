# map(function, iterable)

# Doubling each element in a list using map()
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# filter(function, iterable)
# Filtering even numbers from a list using filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


# reduce(function, iterable)
# Computing the product of elements in a list using reduce()
from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

numbers = [10, 1, 100, 10]
roman_sum = reduce(lambda x, y: x - y if x > y else x + y, numbers)
print(roman_sum)
