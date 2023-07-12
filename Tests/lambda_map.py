# Squaring a number using a lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Doubling a list of numbers using a lambda function with map()
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]
