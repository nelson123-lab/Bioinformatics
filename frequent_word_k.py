from collections import defaultdict
import re

def find_k_most_frequent_words(text, k):
    # Step 1: Define the word boundaries
    word_pattern = r'\b\w+\b'  # Word pattern using word boundaries

    # Step 2: Tokenize the text
    tokens = re.findall(word_pattern, text)

    # Step 3: Count word occurrences and find the k most frequent words
    word_count = defaultdict(int)
    for token in tokens:
        word_count[token] += 1

    sorted_words = sorted(word_count, key=word_count.get, reverse=True)
    k_most_frequent = sorted_words[:k]

    return k_most_frequent

# Example usage
text = "Thisisasampletext.Thistextcontainssomerepeatedwords.Sampletext."
k = 3

frequent_words = find_k_most_frequent_words(text, k)
print(f"The {k} most frequent words in the text are: {frequent_words}")
