lst = [1, 2, 3, 4]
old_elem = 2
new_elem = 10
if old_elem in lst:
    lst[lst.index(old_elem)] = new_elem
