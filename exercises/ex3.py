
def add_numbers(num_list):
    sum = 0

    for num in num_list:
        sum += float(num)
    print(sum)


add_numbers([1.0, 1.1, "1"])
