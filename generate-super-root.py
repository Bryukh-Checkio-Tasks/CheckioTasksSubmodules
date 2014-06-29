# from random import randint
#
# BOTTOM = 1
# TOP = 43
# PREC = 0.001
#
# def super_root(n):
#     low = BOTTOM
#     top = TOP
#     current = (top + low) / 2
#     current_pow = current ** current
#     while not (n - PREC < current_pow < n + PREC):
#         if current_pow > n:
#             top = current
#         else:
#             low = current
#         current = (top + low) / 2
#         current_pow = current ** current
#         # print(current, current_pow)
#     c = 0
#     r = round(current, c)
#     while not (n - PREC < r ** r < n + PREC):
#         c += 1
#         r = round(current, c)
#     return round(current, c+1)
#
# T = [
#     # 4,
#     # 27,
#     # 81,
#     # 1,
#     # 2,
#     # 10**10,
#     # 10**10-1,
#     #
#     5 **5,
#     7 ** 7,
#     9 ** 9,
#     None,
#     None,
#     None,
#     None,
#     None,
#     42
# ]
#
# for t in T:
#     if t is None:
#         t = randint(1, 10**10)
#     p = super_root(t)
#     # print(p)
#     print("""   {{
#         "input": {0},
#         "answer": {0},
#         "show": {1}
#     }},""".format(t, p))

from math import log

def super_root(n):
    if n == 1:
        return 1.
    x, y, z = 5., 0., 0.
    while x != z:
        y, z = x, y
        x = (x + log(n, x)) * .5
    if x ** x < n:
        y = x * (1. + 1.27e-16)
    else:
        y = x * (1. - 1.27e-16)
    for a, b, c in zip(str(int(x ** x)), str(n), str(int(y ** y))):
        if a == b != c:
            break
        elif a != b == c:
            x = y
            break
    print(str(n))
    print(str(int(x ** x)))
    print()
    return x

super_root(10 ** 100 - 100)
super_root(49999999999999999)

N = 100

super_root(N ** N - 100)