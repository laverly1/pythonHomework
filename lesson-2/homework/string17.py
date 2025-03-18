text = input("Enter a string: ")
print("".join("*" if char in "aeiouAEIOU" else char for char in text))
