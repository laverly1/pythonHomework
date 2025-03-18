lst = [1, 2, 3]
n = 3

repeated_lst = []
for x in lst:
    for _ in range(n):
        repeated_lst.append(x)

print(repeated_lst)
