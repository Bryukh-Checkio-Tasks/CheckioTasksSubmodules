from random import randint


def weak_point(matrix):
    lm = len(matrix)
    r = c = lm
    min_row = min_col = float("inf")
    for i, row in enumerate(matrix):
        if sum(row) < min_row:
            r = i
            min_row = sum(row)
    matrix = zip(*matrix)
    for i, row in enumerate(matrix):
        if sum(row) < min_col:
            c = i
            min_col = sum(row)
    # print(r, c)
    return [r, c]


T = [
    # [[7, 2, 7, 2, 8],
    #  [2, 9, 4, 1, 7],
    #  [3, 8, 6, 2, 4],
    #  [2, 5, 2, 9, 1],
    #  [6, 6, 5, 4, 5]],
    # [[7, 2, 4, 2, 8],
    #  [2, 8, 1, 1, 7],
    #  [3, 8, 6, 2, 4],
    #  [2, 5, 2, 9, 1],
    #  [6, 6, 5, 4, 5]],
    # [[1, 1, 1],
    #  [1, 1, 1],
    #  [1, 1, 1]]
    #
    # [[1]],
    # [[9] * 10 for _ in range(10)],
    # [[x % 9 + 1 for x in range(i, i + 10)] for i in range(0, 10)],
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
        l = randint(1, 10)
        t = [[randint(1, 9) for _ in range(l)] for _ in range(l)]
    rows = [sum(row) for row in t]
    cols = [sum(row) for row in zip(*t)]
    ans = weak_point(t)
    print("""{{
    "input": {},
    "answer": {},
    "explanation": [{}, {}],
    }},""".format(t, ans, rows, cols))