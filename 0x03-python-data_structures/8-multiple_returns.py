#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (O, None)
    else:
        # Return string length and first character
        return (len(sentence), sentence[0])
