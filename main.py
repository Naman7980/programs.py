import random

original_string = "The quick brown fox jumps over the lazy dog"
vocabulary = "abcdefghijklmnopqrstwxyz"

# Randomly select 3 unique words
words_to_add = random.sample(vocabulary, 3)

# Join the 3 words into a single string separated by spaces
prefix = "".join(words_to_add)

# Combine the prefix with the original string
new_string = f"{prefix}{original_string}"

print("New string:", new_string)
