#!/usr/bin/python3

""" Custom list class that inherits from built-in list class. """


class MyList(list):
    """
    Initializes a new MyList instance.
    """
    def __init__(self):
        """
        Initiliazes a new MyList instance.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the elements of the list in sorted  order.
        Return:
            Nothing
        """
        print(sorted(self))
