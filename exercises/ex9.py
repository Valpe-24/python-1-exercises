def vowel_counter(sentence):
    sentence_lower = sentence.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0

    for letter in sentence_lower:
        for vowel in vowels:
            if letter == vowel:
                counter += 1
                break
    return f" Number of vowels: {counter}"


sentence = "This is a test"
num_vowels = vowel_counter(sentence)
print(num_vowels)
