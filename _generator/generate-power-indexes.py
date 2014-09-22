from random import randint


def index_power(array, n):
    try:
        return array[n] ** n
    except IndexError:
        return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"

T = [
    # ([1, 2, 3, 4], 2),
    # ([1, 3, 10, 100], 3),
    # ([0, 1], 0),
    # ([1, 2], 3)
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
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
        t = [randint(0, 100) for _ in range(randint(1, 10))], randint(0, 10)

    ans = index_power(*t)
    if ans == -1:
        continue
    print("""{{
    "input": {},
    "answer": {},
    }},""".format(t, ans))