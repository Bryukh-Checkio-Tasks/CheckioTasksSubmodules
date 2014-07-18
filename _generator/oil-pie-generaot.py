from fractions import Fraction as fr
from random import randint


def divide_pie(groups):
    quantity = sum(abs(x) for x in groups)
    results = [fr(1)]

    for g in groups:
        if g < 0:
            results.append(results[-1] * fr(quantity + g, quantity))
        else:
            results.append(results[-1] - fr(g, quantity))
    return [[f.numerator, f.denominator] for f in results]

T = [
    # (2, -1, 3),
    # (1, 2, 3),
    # (-1, -1, -1),
    # (10,),
    #
    # (99, -99),
    # [1] * 99 + [-1],
    None,
    None,
    None,
    None,
    None,
]

for t in T:
    if t is None:
        tl = randint(1, 20)
        t = [x for x in (randint(-99, 99) for _ in range(tl)) if x]
    res = divide_pie(t)
    ans = res[-1]
    show = str(t)
    print("""{{
    "input": {},
    "answer": {},
    "show": "{}",
    "explanation": {}
     }},""".format(t, ans, show, res))

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert isinstance((2, -2), (tuple, list))
#     print(divide_pie((2, -1, 3)))
#     assert tuple(divide_pie((1, 2, 3))) == (0, 1)

