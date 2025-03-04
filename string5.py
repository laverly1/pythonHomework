text = input("Enter a string: ").lower()
vowels = sum(1 for char in text if char in "aeiou")
consonants = sum(1 for char in text if char.isalpha() and char not in "aeiou")
print(f"Vowels: {vowels}, Consonants: {consonants}")
