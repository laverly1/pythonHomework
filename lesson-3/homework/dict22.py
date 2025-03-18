my_dict = {'a': 1, 'b': 2, 'c': 3}

filtered_dict = {}

for key, value in my_dict.items():
    if value > 1:
        filtered_dict[key] = value 

print(filtered_dict)  
