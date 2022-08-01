#!/usr/bin/python3

def calc_equival_point(data, derive):
    default = derive[0]
    result = []
    result.append(1)
    result.append(0)
    for i in range(1, len(data) - 1):
        if (default < derive[i]):
            default = derive[i]
            result[0] = data[i][0]
            result[1] = i
    return result
