
def replace_period(sentence, punct):
    sentence2 = sentence.replace('.', punct)
    return sentence2


# sentence = "Test.  This is a test.  Testing."
# sentence2 = replace_period(sentence, "!")
# print(sentence2)