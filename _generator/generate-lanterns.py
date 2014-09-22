LAND = "X"
WATER = "."

UP = "^"
DOWN = "|"
LEFT = "<"
RIGHT = ">"

DIRS_BANKS = {
    DOWN: ((0, 1), (0, -1)),
    UP: ((0, -1), (0, 1)),
    LEFT: ((1, 0), (-1, 0)),
    RIGHT: ((-1, 0), (1, 0)),
}

DIRS = {
    DOWN: (1, 0),
    UP: (-1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
}

LEFT_TURN = {
    DOWN: RIGHT,
    RIGHT: UP,
    UP: LEFT,
    LEFT: DOWN,
}

RIGHT_TURN = {
    DOWN: LEFT,
    RIGHT: DOWN,
    UP: RIGHT,
    LEFT: UP,
}


def create_stream_maps(wmap):
    lants = [(0, i) for i, ch in enumerate(wmap[0]) if ch == WATER]
    W = len(lants)
    for current in lants[:-1]:
        direction = DOWN
        while True:
            try:
                wmap[current[0]][current[1]] = direction
                new_pos = current[0] + DIRS[direction][0], current[1] + DIRS[direction][1]
                if wmap[new_pos[0]][new_pos[1]] != ".":
                    direction = LEFT_TURN[direction]
                    continue
                right_try_dir = RIGHT_TURN[direction]
                right_try = current[0] + DIRS[right_try_dir][0], current[1] + DIRS[right_try_dir][1]
                if wmap[right_try[0]][right_try[1]] == ".":
                    direction = right_try_dir
                    continue
                current = new_pos
                print()
                for row in wmap:
                    print("".join(row))
            except IndexError:
                break
        for row in wmap:
            print("".join(row))

    current = lants[-1]
    direction = DOWN
    while True:
        try:
            wmap[current[0]][current[1]] = direction
            new_pos = current[0] + DIRS[direction][0], current[1] + DIRS[direction][1]

            left_try_dir = LEFT_TURN[direction]
            left_try = current[0] + DIRS[left_try_dir][0], current[1] + DIRS[left_try_dir][1]
            if wmap[left_try[0]][left_try[1]] == ".":
                direction = left_try_dir
                continue
            if wmap[new_pos[0]][new_pos[1]] != ".":
                direction = LEFT_TURN[direction]
                continue
            current = new_pos
        except IndexError:
            break
    for row in wmap:
        print("".join(row))
    print()
    return wmap


def lanterns_flow(river_map, minutes):
    # make_stream_maps(river_map)
    work_map = [list(row) for row in river_map]
    create_stream_maps(work_map)
    lanterns = [(0, i) for i, ch in enumerate(river_map[0]) if ch == WATER]
    for i, cur in enumerate(lanterns):
        for _ in range(minutes):
            d = work_map[cur[0]][cur[1]]
            cur = cur[0] + DIRS[d][0], cur[1] + DIRS[d][1]
        lanterns[i] = cur
    exp_map = [list(row) for row in river_map]
    for x, y in lanterns:
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                nx, ny = x + i, y + j
                if 0 <= nx < len(exp_map) and 0 <= ny < len(exp_map[0]):
                    exp_map[nx][ny] = "*" if exp_map[nx][ny] != LAND else LAND
    for x, y in lanterns:
        exp_map[x][y] = "0"
    ans = sum(sum(ch == "*" or ch == "0" for ch in row) for row in exp_map)
    # for row in exp_map:
    #     print("".join(row))
    # print(ans)
    return ans, exp_map, work_map


T = [
    # (("X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X......X",
    #   "X......X",
    #   "X......X",
    #   "X......X",
    #   "XXX....X"), 0),
    # (("X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X......X",
    #   "X......X",
    #   "X......X",
    #   "X......X",
    #   "XXX....X"), 7),
    # (("X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X....XXX",
    #   "X......X",
    #   "X......X",
    #   "X......X",
    #   "X......X",
    #   "XXX....X"), 9),
    # (
    #     ("X..X",
    #      "X..X",
    #      "X..X",
    #      "X..X",), 1
    # ),
    # (
    #     ("X.XX",
    #      "X..X",
    #      "XX.X",
    #      "X..X",
    #      "X.XX"), 3
    # ),
    # (
    #     ("XXXXX.X",
    #      "X...X.X",
    #      "X.X...X",
    #      "X.XXXXX",
    #     ), 6
    # ),
    # (
    #     (
    #         "X..XXXXXXX",
    #         "X..X.....X",
    #         "X..X.....X",
    #         "X.....X..X",
    #         "X.....X..X",
    #         "XXXXXXX..X",
    #         "XX.......X",
    #         "XX.......X",
    #         "XX..XXXXXX",
    #     ), 4
    # ),
    # (
    #     (
    #         "X..XXXXXXX",
    #         "X..X.....X",
    #         "X..X.....X",
    #         "X.....X..X",
    #         "X.....X..X",
    #         "XXXXXXX..X",
    #         "XX.......X",
    #         "XX.......X",
    #         "XX..XXXXXX",
    #     ), 12
    # ),
    # (
    #     (
    #         "X..XXXXXXX",
    #         "X..X.....X",
    #         "X..X.....X",
    #         "X.....X..X",
    #         "X.....X..X",
    #         "XXXXXXX..X",
    #         "XX.......X",
    #         "XX.......X",
    #         "XX..XXXXXX",
    #     ), 17
    # ),
    (
        (
            "XXXXXXXXXXXXXXXXXXXXXXX.....X",
            "X...........................X",
            "X...........................X",
            "X...........................X",
            "X...........................X",
            "X...........................X",
            "X.....XXXXXXXXXXXXXXXXXXXXXXX",
            "X.....X.....................X",
            "X.....X.....................X",
            "X.....X.....................X",
            "X.....X.....................X",
            "X.....X.....................X",
            "X.....X.....XXXXXXXXXXX.....X",
            "X...........XXXXXX..........X",
            "X...........XXXXXX..........X",
            "X...........XXXXXX..........X",
            "X...........XXXXXX..........X",
            "X...........XXXXXX..........X",
            "XXXXXXXXXXXXXXXXXX.....XXXXXX",
        ), 70

    )

]

for t in T:
    a, e, d = lanterns_flow(*t)
    print("""{{
    "input": {},
    "answer": {},
    "explanation": [{},
                    {}]
    }},""".format(t, a, e, d))