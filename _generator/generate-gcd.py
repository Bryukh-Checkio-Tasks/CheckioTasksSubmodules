from functools import reduce
from random import randint


def gcd_many(*numbs):
    from fractions import gcd
    return reduce(lambda x,y: gcd(x,y), numbs)

for _ in range(10000):
    numbs_len = randint(2, 10)
    t = [randint(1, 2 ** 32) for _ in range(numbs_len)]
    ans = gcd_many(*t)
    if ans > 2 and len(t) > 3:
        print("""{{
        "input": {},
        "answer": {}
        }},""".format(t, gcd_many(*t)))