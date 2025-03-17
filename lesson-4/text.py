txt = "assalom"
vowels = "aeiou"
result = ""
counter = 0

for char in txt:
    result += char
    counter += 1
    if counter == 3 and char not in vowels:
        result += "_"
        counter = 0

print(result)