lst = [1, 2, 3, 4, 5, 2]

middle_index = len(lst) // 2

if len(lst) % 2 != 0:
    middle = lst[middle_index]
else:
    middle = lst[middle_index - 1: middle_index + 1]

print(middle)
