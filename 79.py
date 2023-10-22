sentences = ["This is a sentence.", "Another sentence here.", "This is a test sentence."]
word_count = {}
for sentence in sentences:
    words = sentence.split()
    for word in words:
        word = word.strip(".,!").lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print("Word counts in the list of sentences:")
print(word_count)
