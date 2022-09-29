#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dict is None or a_dict == {}:
        return None
    _max = max(a_dict.values())
    for key in a_dict:
        if _max == a_dict[key]:
            return key
