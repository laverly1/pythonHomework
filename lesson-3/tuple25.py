tup = (1, 2, 2, 3, 3, 4, 5)

unique_elements = []

for x in tup:
    if x not in unique_elements:
        unique_elements.append(x)

unique_elements_tuple = tuple(unique_elements)

print(unique_elements_tuple)
