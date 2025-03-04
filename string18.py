text = input("Enter sentence: ")
start = input("Starting with: ")
end = input("Ending with: ")
print("Matches" if text.startswith(start) and text.endswith(end) else "Does not match")
