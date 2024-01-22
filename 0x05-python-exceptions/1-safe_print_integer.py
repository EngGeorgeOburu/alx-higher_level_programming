#!/usr/bin/python
def safe_print_interger(value):
    value = 0
    try:
        print("value, {:d}.format(value)")
        return True
    except ValueError:
        return False
