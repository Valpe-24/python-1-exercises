def count_words(sentence):
    word_count = 1
    in_space = False

    for char in sentence:
        if char == " ":
            in_space = True
        elif char != " " and in_space is True:
            word_count += 1
            in_space = False

    return word_count

print(count_words('This  is   a    test'))