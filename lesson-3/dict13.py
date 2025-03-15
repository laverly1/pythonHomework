my_dict = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {}

for key, value in my_dict.items():
    inverted_dict[value] = key

print(inverted_dict)
