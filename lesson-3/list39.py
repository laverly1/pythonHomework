lst = [1, 2, 3, 4, 5]
n = 2

nested_lst = []

for i in range(0, len(lst), n):
    nested_lst.append(lst[i:i + n])

print(nested_lst)
