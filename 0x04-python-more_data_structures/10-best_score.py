#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    mx_score = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if mx_score == value:
            return key
