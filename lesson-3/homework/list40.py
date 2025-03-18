lst = [1, 2, 2, 3, 3, 4, 5]

unique_in_order = []

for x in lst:
    if x not in unique_in_order:
        unique_in_order.append(x)

print(unique_in_order)
