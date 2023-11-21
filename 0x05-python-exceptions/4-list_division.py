#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = list()
    for elem in range(list_length):
        try:
            temp = my_list_1[elem] / my_list_2[elem]
        except TypeError:
            print("wrong type")
            temp = 0
        except ZeroDivisionError:
            print("division by 0")
            temp = 0
        except IndexError:
            print("out of range")
            temp = 0
        finally:
            result.append(temp)
    return result
