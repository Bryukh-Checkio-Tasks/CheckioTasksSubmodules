from random import randint, shuffle, choice


def can_pass(matrix, f, s):
    good = matrix[f[0]][f[1]]
    neighbours = {f}
    visited = set()
    while neighbours:
        x, y = neighbours.pop()
        if (x, y) in visited:
            continue
        if (x, y) == s:
            return True
        visited.add((x, y))
        for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            try:
                nx, ny = x + i, y + j
                if nx >= 0 and ny >= 0 and matrix[nx][ny] == good and (nx, ny) not in visited:
                    neighbours.add((nx, ny))
            except IndexError:
                continue
    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'

T = [
    [[
         [0, 0],
         [0, 0]],
     [0, 0], [1, 1]
    ],
    [[
         [1, 9],
         [9, 1]],
     [0, 1], [1, 0]
    ],
    [[
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 2, 2, 2, 2, 2, 2, 1, 0],
         [0, 1, 0, 3, 0, 0, 3, 0, 1, 0],
         [0, 1, 0, 3, 0, 4, 3, 0, 1, 0],
         [0, 1, 0, 3, 0, 0, 3, 0, 1, 0],
         [0, 1, 0, 3, 4, 0, 3, 0, 1, 0],
         [0, 1, 0, 3, 0, 0, 3, 0, 1, 0],
         [0, 1, 0, 3, 0, 4, 3, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ], [0, 0], [2, 6]],
    [
        [
            [9] * 10,
            [9] * 10,
            [9] * 10,
            [9] * 10,
            [9] * 10,
            [9] * 10,
            [9] * 10,
            [9] * 10,
            [9] * 10,
            [9] * 10
        ],
        [0, 9], [9, 0]
    ],
    [
        [
            [5, 6],
            [6, 6],
            [6, 5],
            [6, 6],
            [7, 6],
            [6, 6],
            [6, 7],
            [6, 6],
            [8, 6],
            [6, 6],
        ], [9, 1], [0, 1]
    ]


]

T = [
    None] * 100

for t in T:
    if t is None:
        w = randint(2, 10)
        h = randint(2, 10)
        div = randint(3, 10)
        numbs = list(range(0, 10))
        shuffle(numbs)
        numbs = numbs[:div]
        matr = [[choice(numbs) for _ in range(w)] for _ in range(h)]
        f = (randint(0, h - 1), randint(0, w - 1))
        s = (randint(0, h - 1), randint(0, w - 1))
        if f == s: continue
        if matr[f[0]][f[1]] != matr[s[0]][s[1]]: continue
        t = [matr, f, s]
    ans = can_pass(t[0], tuple(t[1]), tuple(t[2]))
    if not ans: continue
    print("""{{
    "input": {},
    "answer": {}
    }},""".format(t, ans))