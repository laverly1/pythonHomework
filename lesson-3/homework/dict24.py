tuple_data = (('a', 1), ('b', 2), ('c', 3))

my_dict = {}

for item in tuple_data:
    key, value = item 
    my_dict[key] = value  

print(my_dict) 