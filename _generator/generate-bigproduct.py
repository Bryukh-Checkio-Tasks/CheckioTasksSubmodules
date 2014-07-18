from random import randint


def prod(l):
    r = 1
    for x in l:
        r *= x
    return r


def solution(array, n):
    return max(prod(array[i:i + n]) for i in range(len(array) - n + 1))

T = [
    # [[1], 1],
    # [[1] * (10 ** 4), 1],
    # [[1] * (10 ** 4), 10**4],
    # [[randint(1, 99) for x in range(10 ** 4)], 2],
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]


for t in T:
    if t is None:
        n = randint(2, 10)
        l = [randint(1, 100) for x in range(100)]
        t = [l, n]
    ans = solution(*t)
    print("""{{
        "input": {},
        "answer": {},
    }},""".format(t, ans))

# for i in range(100):
#     n = randint(2, 10)
#     l = [randint(1, 100) for x in range(100)]
#     TESTS["Small"].append({"input": (l, n), "answer": f(l, n)})
# for i in range(10):
#     n = randint(2, 10)
#     l = [randint(1, 100) for x in range(10 ** 4)]
#     TESTS["Big"].append({"input": (l, n), "answer": f(l, n)})