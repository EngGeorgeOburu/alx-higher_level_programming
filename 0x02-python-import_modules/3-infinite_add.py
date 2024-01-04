#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv[0] is the script name
    name_script = sys.argv[0]

    # sys.argv[1:] contains the command line arguments
    arguments = sys.argv[1:]

    # This converts the arguments to integrer and add them
    total = sum(int(arg) for arg in arguments)

    print("{}".format(total))
