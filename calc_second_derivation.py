#!/usr/bin/python3
import tools

def calc_second_derivative(derive, file):
    stk1 = 0
    stk2 = 0
    h1 = 0
    h2 = 0
    res = 0
    second_derive = []

    print("Second derivative:")
    second_derive.append(0)
    second_derive.append(0)
    for i in range(2, len(derive) - 2):
        h1 = (file[i + 1][0] - file[i][0])
        if (h1 == 0):
            exit(84)
        stk1 = (derive[i + 1] - derive[i]) / h1
        h2 = (file[i][0] - file[i - 1][0])
        if ((h2 == 0)):
            exit(84)
        stk2 = (derive[i] - derive[i - 1]) / h2
        if (h1 + h2) == 0:
            exit(84)
        res = (((stk1 * h2) + (stk2 * h1)) / (h1 + h2))
        second_derive.append(res)
        print("%.1f ml -> %.2f" % (file[i][0], res))
    print("")
    return (second_derive)