my_dict = {'a': 1, 'b': 2, 'c': 1}
value = 1

keys_with_value = []

for key, val in my_dict.items():
    if val == value:
        keys_with_value.append(key)

print(keys_with_value)  
