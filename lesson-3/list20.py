lst = [1, 2, 3, 4, 5]
unique_lst = list(set(lst))
unique_lst.sort()
second_largest = unique_lst[-2] if len(unique_lst) > 1 else None
