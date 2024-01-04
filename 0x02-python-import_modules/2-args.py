#!/usr/bin/python3
from sys import argv #Import the argv module sys package

if __name__ == "__main__": #check if the scrpt is being run direclty
    argc = len(argv) - 1
    ifargc == 0:
        print("O arguments.")
    elif argc == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(argc))
for i in range(argc):
    print("{}: {}".format(1 + 1, sys.argv[i + 1]))



