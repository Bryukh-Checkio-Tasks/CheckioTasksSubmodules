from itertools import combinations
from random import randint


def golf(coins):
    possible = set()
    ranged = set(range(1, sum(coins) + 2))
    for cl in range(len(coins) + 1):
        for var in combinations(coins, cl):
            possible.add(sum(var))
    return min(ranged.difference(possible))


T = [
    # [1] * 10,
    # list(range(1, 10)),
    # list(range(9, 0, -1)),
    # [9] * 10,
    # [1]
    #
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

for t in T:
    if not t:
        t = [randint(1, 9) for _ in range(randint(3, 10))]

    ans = golf(t)
    if ans == sum(t) + 1:
        continue
    print("""
        {{
            "input": {},
            "answer": {},
        }},""".format(t, ans))