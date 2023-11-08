#!/usr/bin/python3

def weight_average(my_list=[]):
    average = 0
    numerator = 0
    denominator = 0
    for item in my_list:
        numerator += (item[0] * item[1])
        denominator += item[1]
    else:
        average = numerator / denominator

    return average
