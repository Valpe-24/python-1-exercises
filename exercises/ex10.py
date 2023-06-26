def calculator():  # Create a function with NO parameters
    number = int(input("Enter number 1: "))  # Read input from user and cast it as an int
    number_2 = int(input("Enter number 2: "))  # Read input #2 from user and cast it as an int
    operation = input("Enter operation (+, *, /, -): ") # Read operation from user
    if operation == "+":  # condition #1 if operation is '+'
        return number + number_2  # return sum of the 2 numbers

    elif operation == "-":  # condition #2 if operation is '-'
        return number - number_2  # return subtraction of the 2 numbers
    elif operation == "*":  # condition #3 if operation is '*'
        return number * number_2  # return multiplication of the 2 numbers
    elif operation == "/":  # condition #4 if operation is '/'
        return number / number_2  # return division of the 2 numbers
    else:
        return 'Operation not valid. Try again'  # return is not valid if sign is not an operation


while True:  # while true keep asking user for input to repeat the program
    result = calculator()
    print(result)