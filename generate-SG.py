from itertools import permutations
from random import randint

def golf(holes):
    best = float("inf")
    route = []
    for var in permutations(holes):
        prev = (0, 0)
        dist = 0
        for h in var:
            dist += ((prev[0] - h[0]) ** 2 + (prev[1] - h[1]) ** 2) ** 0.5
            prev = h
        if dist < best:
            best = dist
            route = var
    return best, route

def rand_set():
    res = set()
    while len(res) < 5:
        res.add((randint(1, 9), randint(1, 9)))
    return res

TESTS = [
    {(1, 1), (1, 9), (9, 1), (9, 9), (5, 9)},
    {(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)},
    {(1, 1), (3, 1), (5, 1), (7, 1), (9, 1)},
]

for t in TESTS:
# for _ in range(20):
#     t = rand_set()
    ans, exp = golf(set(t))
    print('{{\n\t"input": {},\n\t"answer": {},\n\t"show": {},\n\t"explanation": {},}}'.format(t, ans, round(ans, 2), exp))
