def multiplier(n):
    return lambda x : x * n

m = multiplier(30)

print(m(3))
print(m(7))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

