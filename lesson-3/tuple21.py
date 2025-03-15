tup = (1, 2, 3)
n = 3

repeated_elements = []

for x in tup:
    for _ in range(n):
        repeated_elements.append(x)

repeated_tuple = tuple(repeated_elements)

print(repeated_tuple)
