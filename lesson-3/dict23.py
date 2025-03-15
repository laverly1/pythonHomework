dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1_keys = set(dict1.keys())
dict2_keys = set(dict2.keys())

common_keys = dict1_keys & dict2_keys

print(common_keys)  