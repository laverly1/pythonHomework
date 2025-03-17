list1 = [1, 1, 2]
list2 = [2, 3, 4]

result = []
for x in list1:
    if (list1.count(x) != list2.count(x)):
        result.append(x)
for x in list2:
    if (list1.count(x) != list2.count(x)):
        result.append(x)

print(result)
