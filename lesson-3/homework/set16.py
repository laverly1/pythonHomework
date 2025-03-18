my_set = {1, 2, 3, 4, 5}

even_set = set()

for x in my_set:
    if x % 2 == 0:
        even_set.add(x)

print(even_set)
