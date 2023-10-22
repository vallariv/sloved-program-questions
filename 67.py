text = "This is a sample text. This text contains sample words."
words = text.split()
word_frequency = {}
for word in words:
    word = word.strip(".,!").lower()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequencies in the text:")
print(word_frequency)
