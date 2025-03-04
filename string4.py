text = input("Enter a string: ").replace(" ", "").lower()  
print("Palindrome" if text == text[::-1] else "Not a palindrome")
