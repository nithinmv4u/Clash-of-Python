numbers = [1, 2, 3, 4, 5]
even_numbers =0
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))

print(squares)

squares = [x**2 for x in range(10)]

print(squares)