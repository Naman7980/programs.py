import random

original_string = input("enter word you want to convert into secret word: ")
vocabulary = "abcdefghijklmnopqrstwxyz"


original_string = original_string[1:] + original_string[0]

# Randomly select 3 unique words
words_to_add = random.sample(vocabulary, 3)

# Join the 3 words into a single string separated by spaces
prefix = "".join(words_to_add)

# Combine the prefix with the original string
new_string = f"{prefix}{original_string}{prefix}"

print("New string:", new_string)