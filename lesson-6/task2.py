import os
import string
from collections import Counter

def create_sample_file():
    """Prompt the user to create sample.txt if it doesn't exist."""
    text = input("sample.txt not found. Please enter a paragraph to create the file: ")
    with open("sample.txt", "w") as file:
        file.write(text)

def read_file():
    """Read the content of sample.txt, creating it if necessary."""
    if not os.path.exists("sample.txt"):
        create_sample_file()
    
    with open("sample.txt", "r") as file:
        return file.read()

def count_words(text):
    """Count word frequency in the given text."""
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_count = Counter(words)
    return word_count

def generate_report(word_count):
    """Generate a word count report and save it to word_count_report.txt."""
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)
    
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")
    
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

def main():
    text = read_file()
    word_count = count_words(text)
    generate_report(word_count)
    print("Report saved to word_count_report.txt")

if __name__ == "__main__":
    main()
