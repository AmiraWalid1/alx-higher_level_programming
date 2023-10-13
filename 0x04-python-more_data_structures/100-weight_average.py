#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_score = sum_weight = 0
    for my_tuple in my_list:
        sum_score += (my_tuple[0] * my_tuple[1])
        sum_weight += my_tuple[1]
    return sum_score / sum_weight
