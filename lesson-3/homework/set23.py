import random

random_set = set()

for _ in range(10):
    random_integer = random.randint(1, 100)
    random_set.add(random_integer)

print(random_set)
