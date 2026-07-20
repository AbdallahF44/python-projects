a = [1, 2, 3, 4]
b = [x for x in a]
print(b)
a = [1, 2, 3, 4]
b = [x for x in range(len(a)) if a[x] % 2 == 0]
print(b)
a = [1, 2, 3, 4]
b = [x for x in a if x % 2 == 0]
print(b)

d = {x: y for (x, y) in zip(a, b)}
print(list(zip(a, b)))
print(d)
