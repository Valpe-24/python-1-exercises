from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12, ex13


def main():
    # EX1
    ex1.hello_world("3")

    # EX2
    ex2.array_to_string([1, 2, 3])

    # EX 3
    ex3.add_numbers([1.0, 1.1, "1"])

    # EX4
    sentence = input("Enter sentence: ")
    num_words = ex4.count_words(sentence)
    print(num_words)

    # EX5
    sentence_1 = "Test.  This is a test.  Testing."
    sentence2 = ex5.replace_period(sentence_1, "!")
    print(sentence2)

    # EX6
    ex6.slice_it_2(["this", "is", "another", "test"])

    # EX7
    result1 = ex7.calc_total([2.00, 4.00, 4.00], "10%")
    print(result1)

    # EX8
    print(ex8.f_to_c(22))
    print(ex8.c_to_f(-6))

    # EX9
    sentence = "This is a test"
    num_vowels = ex9.vowel_counter(sentence)
    print(num_vowels)

    # EX11
    ex11.diagonal_printer("this is a test")

    # EX12
    ex12.word_histogram("three three three two two one")

    # EX13
    wordlist = ["Hello", "World", "in", "a", "frame"]
    ex13.frame_it(wordlist)

    # EX10
    while True:
        result = ex10.calculator()
        print(result)


if __name__ == '__main__':
    main()
