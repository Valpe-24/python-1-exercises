def diagonal_printer(str):  # Create a function that takes a string parameter
    list_str = str.split()  # split the words and save them in a list

    for word in list_str:  # loop thru each word of the list
        for i in range(len(word)):  # loop thru each letter of each word
            print(' ' * i, word[i])  # multiply space by the position of the letter in the word and then print letter


diagonal_printer("this is a test")   # calling the function
