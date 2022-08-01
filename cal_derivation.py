
#!/usr/bin/python3
import tools

def equivalent_point(derive, file):
    equival = tools.calc_equival_point(file, derive)
    derive.append(0)
    print("\nEquivalence point at %.1f ml\n" % equival[0])
    return (equival[0])

def cal_derivate(file):
    stk1 = 0
    stk2 = 0
    h1 = 0
    h2 = 0
    derive = []
    derive.append(0)

    print("Derivative:")
    for i in range(1, len(file) - 1):
        h1 = (file[i + 1][0] - file[i][0])
        if (h1 == 0):
            exit(84)
        stk1 = (file[i + 1][1] - file[i][1]) / h1
        h2 = (file[i][0] - file[i - 1][0])
        if (h2 == 0):
            exit(84)
        stk2 = (file[i][1] - file[i - 1][1]) / h2
        if (h1 + h2) == 0:
            exit(84)
        derive.append(((stk1 * h2) + (stk2 * h1)) / (h1 + h2))
        print("%.1f ml -> %.2f" %(file[i][0], derive[i]))
    return (derive)
