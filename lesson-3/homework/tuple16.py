tup = (1, 2, 3, 4, 5)

is_sorted = True

for i in range(len(tup) - 1):
    if tup[i] > tup[i + 1]:
        is_sorted = False
        break

print(is_sorted)
