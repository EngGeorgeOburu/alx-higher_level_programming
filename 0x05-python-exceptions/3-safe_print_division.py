#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroIndexError:
        continue
    finally:
        print("Inside results:{}".format(result))
    return result
