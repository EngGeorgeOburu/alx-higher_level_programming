#!/usr/bin/python3
if __name__ == "__main__":
    # import functions add,mul, sub and div from calculator_1 module
    from calculator_1 import add, sub, mul, div

    # Assign values to variables a and b
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print('{} - {} = {}'.format(a, b, sub(a, b)))
    print('{} * {} = {}'.format(a, b, mul(a, b)))
    print('{} / {} = {}'.format(a, b, div(a, b)))
