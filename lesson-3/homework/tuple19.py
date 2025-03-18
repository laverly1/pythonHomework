tup = (1, 2, 3, 4, 5)
elem = 3

new_elements = []

for x in tup:
    if x != elem:
        new_elements.append(x)

new_tuple = tuple(new_elements)

print(new_tuple)
