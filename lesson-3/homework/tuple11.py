tup = (1, 2, 2, 3, 4)
elem = 2

indices = []

for i, x in enumerate(tup):
    if x == elem:
        indices.append(i)

print(indices)
