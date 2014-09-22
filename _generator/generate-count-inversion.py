from random import shuffle, randint


def count_inversion(sequence):
    res = 0
    for i, f in enumerate(sequence):
        for s in sequence[i + 1:]:
            res += f > s
    return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"

T = [
    (1, 2, 5, 3, 4, 7, 6),
    (0, 1, 2, 3),
    (99, -99),
    (5, 3, 2, 1, 0),

]

T = [
    tuple(range(-99, 100)),
    tuple(range(99, -100, -1)),
    (0, 1),
    (1, 0),

]

T = [
    None,
    None,
    None,
    None,
    None,
    None,
]

for t in T:
    if t is None:
        t = list(range(-99, 100))
        shuffle(t)
        t = tuple(t[:randint(2, 199)])
    ans = count_inversion(t)
    print("""{{
    "input": {},
    "answer": {}
    }},""".format(t, ans))