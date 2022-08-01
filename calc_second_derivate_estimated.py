#!/usr/bin/python3
import tools

def second_derivate_estimated(file, second_derive, equivalent_point):
    i = 2
    k = 0
    j = 0
    b = 0
    a = 0
    second_derivate_estimated = []
    z = []
    print("Second derivative estimated:")
    while file[i][0] != equivalent_point:
        i = i + 1
    k = (((file[i + 1][0] - file[i - 1][0]) * 10) + 1) * 2
    x = file[i - 1][0] * 10
    while (x / 10) <= equivalent_point:
        z.append(x / 10)
        b = (file[i - 1][0] * second_derive[i]) - (file[i][0] * second_derive[i - 1])
        b = b / (file[i - 1][0] - file[i][0])
        a = (second_derive[i - 1] - second_derive[i]) / (file[i - 1][0] - file[i][0])
        a = a * (x / 10)
        second_derivate_estimated.append((a + b))
        print("%.1f ml -> %.2f" %((x / 10), (a + b)))
        x = x + 1
    while ((x / 10) <= file[i + 1][0]):
        z.append(x / 10)
        b = (file[i][0] * second_derive[i + 1]) - (file[i + 1][0] * second_derive[i])
        b = b / (file[i][0] - file[i + 1][0])
        a = (second_derive[i] - second_derive[i + 1]) / (file[i][0] - file[i + 1][0])
        a = a * (x / 10)
        second_derivate_estimated.append((a + b))
        print("%.1f ml -> %.2f" %((x / 10), (a + b)))
        x = x + 1
    i = 1
    while (i < len(second_derivate_estimated)):
        if (second_derivate_estimated[i] < 0):
            second_derivate_estimated[i] = second_derivate_estimated[i] * (-1)
        i = i + 1
    i = 1
    while (i < len(second_derivate_estimated)):
        if (second_derivate_estimated[i - 1] > second_derivate_estimated[i]):
            equivalent_point = z[i]
        i = i + 1
    print("\nEquivalence point at %.1f ml" %(equivalent_point))