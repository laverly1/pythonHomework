lst = [1, 2, 3, 2, 4]
elem = 2

indices = []
for i, x in enumerate(lst):
    if x == elem:
        indices.append(i)

print(indices)
