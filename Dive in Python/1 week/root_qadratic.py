"""Модуль расчитывает корень квадратного уравнения"""

import sys
import math


def root_calc(a, b, c):
    sq = (b ** 2) - (4 * a * c)
    x1 = int((-b - math.sqrt(sq)) / (2 * a))
    x2 = int((-b + math.sqrt(sq)) / (2 * a))
    return [x1, x2]

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    result = root_calc(a, b, c)
    print("X1 = " + str(result[0]) + "\n" + "X2 = " + str(result[1]))
