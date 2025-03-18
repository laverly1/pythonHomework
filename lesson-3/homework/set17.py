my_set = {1, 2, 3, 4, 5}

odd_set = set()

for x in my_set:
    if x % 2 != 0:
        odd_set.add(x)

print(odd_set)
