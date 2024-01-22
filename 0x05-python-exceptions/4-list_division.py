#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Initialize new list to store new variables """
    new_list = []
    """ Iterate through the range of list length """
    for i in range(list_length):
        try:
            div_result = (my_list_1[i] / my_list_2[i])
        except TypeError:
            div_result = 0
            print("wrong type")
        except ZeroDivisionError:
            div_result = 0
            print("division by 0")
        except IndexError:
            div_result = 0
            print("out of range")
        finally:
            new_list.append(div_result)
    return new_list
