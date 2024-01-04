#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    # Get list of names in the hidden_4 module
    all_names = dir(hidden_4)

    # iterate through each name
    for name in all_names:
        # check if the name doesn't start with "__"
        if not name.startwith("__"):
            print(name)
