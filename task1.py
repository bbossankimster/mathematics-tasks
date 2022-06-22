from sympy.utilities.iterables import multiset_permutations
import math


def climb(hight):
    steps_by_2 = int(hight // 2)
    if hight % 2 == 1:
        tail = "1"
    else:
        tail = ""
    for n in range(1, steps_by_2 + 1):
        rest = steps_by_2 - n
        string_21 = "2"*n + "11"*rest + tail
        for val in multiset_permutations(string_21):
            yield "".join(val)
    yield hight*"1"