import string

my_string = "Hello, world! This is a test string."
no_punctuation_string = my_string.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", no_punctuation_string)
