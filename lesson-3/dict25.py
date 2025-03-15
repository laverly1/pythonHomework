my_dict = {'a': 1, 'b': 2, 'c': 3}

iterator = iter(my_dict.items())  
first_key_value_pair = next(iterator) 

print(first_key_value_pair)  
