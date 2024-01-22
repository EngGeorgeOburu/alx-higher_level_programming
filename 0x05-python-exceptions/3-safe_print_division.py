#!/usr/bin/python3
def safe_print_division(a, b):
    """Initialize the result variable """
    result = None
    try:
        """ Try to perform the division """
        result = a / b
    """ Handles the ZeroDivisionError """
    except ZeroDivisionError:
        """ Does nothing if ZeroDivisionError occurs """
        pass
    finally:
        print("Inside results:{}".format(result))
    return result
