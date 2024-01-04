#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # check if the correct number of cml arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        # convert the input values to integrs
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        # perform the calculations
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            result = div(a, b)
        else:
            print("Uknown operator. Available operators: +, -, * and /")
            sys.exit(1)

            print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
