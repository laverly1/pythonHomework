tup = (1, 2, 3, 4, 5)

nested_elements = []

for i in range(0, len(tup), 2):
    subtuple = tup[i:i+2]
    nested_elements.append(subtuple)

nested_tuple = tuple(nested_elements)

print(nested_tuple)
