def calc_total(array, tax):  # Create a function with 2 parameters: a list of prices and a string tax
    total = 0   # Declare a variable for the sum of all elements on the list
    tax_num = int(tax.replace("%", ""))  # turn tax string into an int and remove '%'
    total_price = 0.0  # Declare variable to calculate total price including taxes

    for price in array:  # start iterations
        total += price  # Adding all the number inside of the list together
    total_price = "${:,.2f}".format(total * (tax_num/100) + total)  # Calculate the total price with taxes AND format to add '$' and trim float number to 2 decimals
    return total_price  # Return total price


array = [2.00, 4.00, 4.00]
tax = "10%"
result = calc_total(array, tax)
print(result)