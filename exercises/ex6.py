# def slice_it(strings):
#     new_string = ''
#
#     for word in strings:
#         new_string += word[0] + word[1]
#     return new_string


def slice_it_2(string):  # Creating a function with a list parameter
    new_string = ''  # Declaring a variable as an empty string
    for word in string:
        new_string += word[0:2]  # taking first 2 letters of each word and adding them to the empty string
    return new_string  # Returning the new word made out of the first 2 letters of each word


print(slice_it_2(["this", "is", "another", "test"]))

