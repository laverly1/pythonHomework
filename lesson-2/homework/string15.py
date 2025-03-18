sentence = input("Enter a phrase: ")
acronym = "".join(word[0].upper() for word in sentence.split())
print(acronym)
