def slide(m, r, c, dr, dc):
    if m[r][c] == m[r+dr][c+dc]:
        m[r][c] = 0
        m[r+dr][c+dc] *= 2
        return 2
    elif m[r+dr][c+dc] == 0:
        m[r+dr][c+dc] = m[r][c]
        m[r][c] = 0
        return 1
    else:
        return 0

def checkio(a, b):
    x = [[0 for c in range(4)] for r in range(4)]

    done = False
    if b == "up":
        for c in range(4):
            for r in range(1, 4):
                t = r
                if a[t][c] == 0:
                    continue
                stop = False
                while t > 0 and x[t-1][c] == 0:
                    z = slide(a, t, c, -1, 0)
                    if z == 0:
                        break
                    done = True
                    if z == 2:
                        stop = True
                    t -= 1
                if stop:
                    x[t][c] = 1
    if b == "down":
        for c in range(4):
            for r in range(1, 4):
                t = 3 - r
                if a[t][c] == 0:
                    continue
                stop = False
                while t < 3 and x[t+1][c] == 0:
                    z = slide(a, t, c, 1, 0)
                    if z == 0:
                        break
                    done = True
                    if z == 2:
                        stop = True
                    t += 1
                if stop:
                    x[t][c] = 1
    if b == "left":
        for r in range(4):
            for c in range(1, 4):
                t = c
                if a[r][t] == 0:
                    continue
                stop = False
                while t > 0 and x[r][t-1] == 0:
                    z = slide(a, r, t, 0, -1)
                    if z == 0:
                        break
                    done = True
                    if z == 2:
                        stop = True
                    t -= 1
                if stop:
                    x[r][t] = 1
    if b == "right":
        for r in range(4):
            for c in range(1, 4):
                t = 3 - c
                if a[r][t] == 0:
                    continue
                stop = False
                while t < 3 and x[r][t+1] == 0:
                    z = slide(a, r, t, 0, 1)
                    if z == 0:
                        break
                    done = True
                    if z == 2:
                        stop = True
                    t += 1
                if stop:
                    x[r][t] = 1

    if done:
        for i in range(15, -1, -1):
            r = i // 4
            c = i % 4
            if a[r][c] == 0:
                a[r][c] = 2
                break

    return a

from random import choice
from copy import deepcopy

MOVES = ["up", "down", "right", "left"]

NUMBERS = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

for _ in range(10):
    m = [[choice(NUMBERS) for _ in range(4)] for _ in range(4)]
    act = choice(MOVES)
    ans = checkio(deepcopy(m), act)
    if m == ans:
        ans = "LOSE"
    print("""{{
    "input": {},
    "answer": {}
}}""".format((m, act), ans))
