#!/usr/bin/python3
from sys import argv # Import the argv module sys package

if __name__ == "__main__": # check if the scrpt is being run direclty
    argc = len(argv) - 1 # Calculate the number of arguements, exclude script name
    if argc == 0:
        print("O arguments.")
    elif argc == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(argc))
# Loops throughs the arguements using range
for i in range(1, argc + 1):
    print("{}: {}".format(i, argv[i]))



