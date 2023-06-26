
def c_to_f(c):
    f = round((c * 9 / 5) + 32)
    print_temp = f"{c} degrees Celsius is {f} degrees Fahrenheit."
    return print_temp

def f_to_c(f):
    c = round((f - 32) * 5/9)
    print_temp = f"{f} degrees Fahrenheit is {c} degrees Celsius."
    return print_temp


print(f_to_c(22))
print(c_to_f(-6))

