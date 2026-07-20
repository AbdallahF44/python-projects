# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]
# new_list = [x for x in thislist if x.startswith("a")]
# print(new_list)

# l2 = [x for x in range(1, int(input()) + 1)]
# print(l2)

# l2.sort(reverse=True)
# l3 = l2
# print(l3)
# print(l3 is l2)

# l2.sort(reverse=True)
# l3 = l2.copy()
# print(l3)
# print(l3 is l2)

# l4 = [x for x in l2]
# print(l4)
# print(l4 is l2)


t1 = 1
print(type(t1))
t2 = (1,)
print(type(t2))
t3 = tuple((1,))
print(type(t3))

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
thistuple = ("apple", "banana", "cherry")
y = dict(enumerate(thistuple))
y[len(y)] = "orange"
thistuple = tuple(y.values())
print(thistuple)

print(tuple(enumerate(thistuple)))

fruits = ("apple", "banana", "cherry")

green, yellow, red = fruits

print(green)
print(yellow)
print(red)

print(type(green))
print(type(yellow))
print(type(red))

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

green, yellow, *red = fruits

print(green)
print(yellow)
print(red)

l1 = [1, 2] * 3
print(l1)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"", False, 0}

print(thisset)

list1 = [x for x in range(1, 11)]
s1 = set(list1)
print(s1)
print(s1.pop())
print(list1)
[print(x, y) for x, y in {1: 2, 3: 4}.items()]
[print(x) for x in {1: 2, 3: 4}.values()]


def myfunc():
    x = 300
    print(x)


myfunc()
# print(x)

numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(type(doubled))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[0])
print(sorted_students)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(2))


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Get first 100 Fibonacci numbers
gen = fibonacci()
for i in range(100):
    print(next(gen))
