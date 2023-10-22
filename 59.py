my_string = "Hello, World!"
vowels = 0
consonants = 0
for char in my_string:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
