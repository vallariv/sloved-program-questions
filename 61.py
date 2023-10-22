sentence = "This is a sample sentence with some long words"
words = sentence.split()
largest_word = max(words, key=len)
print("Largest word in the sentence:", largest_word)
