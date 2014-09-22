from random import randint, random


def mark_land_zones(wmap):
    for i, row in enumerate(wmap):
        for j, ch in enumerate(row):
            if ch == "X":
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        nx, ny = i + x, j + y
                        if 0 <= nx < len(wmap) and 0 <= ny < len(row) and wmap[nx][ny] != "X":
                            wmap[nx][ny] = "S"


def finish_map(region_map):
    d_cells = sum([[(i, j) for j, _ in enumerate(row) if region_map[i][j] == "D"]
                   for i, row in enumerate(region_map)], [])
    work_map = list(list(row) for row in region_map)
    mark_land_zones(work_map)
    # for row in work_map:
    #     print(row)
    for start in d_cells:
        work_map[start[0]][start[1]] = "."
        stack = [start]
        while stack:
            cx, cy = stack.pop()
            if work_map[cx][cy] == "D":
                continue
            work_map[cx][cy] = "D"
            for x, y in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
                if 0 <= x < len(work_map) and 0 <= y < len(work_map[x]) and work_map[x][y] == ".":
                    stack.append((x, y))
    for i, row in enumerate(work_map):
        for j, ch in enumerate(row):
            if work_map[i][j] == ".":
                work_map[i][j] = "S"
    work_map = ["".join(row) for row in work_map]
    # for row in work_map:
    #     print(row)

    return ["".join(row) for row in work_map]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert finish_map(("D..XX.....",
                       "...X......",
                       ".......X..",
                       ".......X..",
                       "...X...X..",
                       "...XXXXX..",
                       "X.........",
                       "..X.......",
                       "..........",
                       "D...X....D")) == ["DDSXXSDDDD",
                                          "DDSXSSSSSD",
                                          "DDSSSSSXSD",
                                          "DDSSSSSXSD",
                                          "DDSXSSSXSD",
                                          "SSSXXXXXSD",
                                          "XSSSSSSSSD",
                                          "SSXSDDDDDD",
                                          "DSSSSSDDDD",
                                          "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",)))

T = [
    # ("D..XX.....",
    #  "...X......",
    #  ".......X..",
    #  ".......X..",
    #  "...X...X..",
    #  "...XXXXX..",
    #  "X.........",
    #  "..X.......",
    #  "..........",
    #  "D...X....D"),
    # ("........",
    #  "........",
    #  "X.X..X.X",
    #  "........",
    #  "...D....",
    #  "........",
    #  "X.X..X.X",
    #  "........",
    #  "........",)
    # (
    #     ".....",
    #     ".....",
    #     "..D..",
    #     ".....",
    #     ".....",
    # ),
    # (
    #     "D...D",
    #     ".....",
    #     "..X..",
    #     ".....",
    #     "D...D",
    # ),
    # (
    #     "XXXXXXX",
    #     "X.....X",
    #     "X..D..X",
    #     "X.DDD.X",
    #     "X..D..X",
    #     "X.....X",
    #     "XXXXXXX",
    # ),
    # (
    #     "...",
    #     ".D.",
    #     "...",
    # ),
    # (
    #     "..........",
    #     "..........",
    #     "..........",
    #     "..........",
    #     "..........",
    #     "..........",
    #     "..........",
    #     "..........",
    #     "..........",
    #     "..........",
    #     ".........D",
    # ),
    # (
    #     "D.XXXXXXXX",
    #     "..XXXXXXXX",
    #     "XXXXXXXXXX",
    #     "XXXXXXXXXX",
    #     "XXXXXXXXXX",
    #     "XXXXXXXXXX",
    #     "XXXXXXXXXX",
    #     "XXXXXXXXXX",
    #     "XXXXXXXX..",
    #     "XXXXXXXX.D",
    # ),
    # (
    #     "DDD",
    #     "DDD",
    #     "D.D",
    #     "DDD",
    #     "DDD",
    # ),
    # (
    #     "..........",
    #     ".D.......X",
    #     "..........",
    #     "..........",
    #     "......X...",
    #     "..........",
    #     "..........",
    #     "...X......",
    #     "..........",
    #     "..........",
    #     "X.........",
    # ),
    # (
    #     "D.........",
    #     "..........",
    #     "..XXXXXX..",
    #     "..X....X..",
    #     "..X....X..",
    #     "..X.......",
    #     "..X.......",
    #     "..XXX.....",
    #     ".........X",
    #     "..........",
    #     "......X...",
    # ),
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
        w = randint(7, 10)
        h = randint(7, 10)
        m = [["." if random() > 0.2 else "X" for _ in range(w)] for _ in range(h)]
        m[randint(0, h-1)][randint(0, w - 1)] = "D"
        t = tuple(["".join(row) for row in m])
    ans = finish_map(t)
    print("""{{
    "input": {},
    "answer": {},
    }},""".format(t, ans))