from itertools import combinations
import random


def state(data):
    robots = {}
    switched = set()
    for pair in data:
        switched.add("-".join(sorted(pair)))
        r1, r2 = pair
        robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)
    return robots

NAMES = [
    "scout",
    "super",
    "digger",
    "melter",
    "planer",
    "driller",
    "hammer",
    "lister",
    "drawer",
    "hater"
]

PAIRS = [list(p) for p in combinations(NAMES, 2)]

for i in range(1, len(PAIRS) + 1):
    # N = random.randint(1, len(PAIRS) - 1)
    N = i
    random.shuffle(PAIRS)
    t = PAIRS[:N]
    print("""{{
    "input": {},
    "answer": {},
    "show": "{}",
    "state": {}
    }},""".format(t, t, tuple(set(p) for p in t), state(t)))