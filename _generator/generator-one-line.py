def create_matrix(lines, points):
    res = [[0] * len(points) for _ in range(len(points))]
    for seg in lines:
        f, s = seg[0:2], seg[2:4]
        i = points.index(f)
        j = points.index(s)
        res[i][j] = res[j][i] = 1
    return res


def copy_matrix(matrix):
    return [row[:] for row in matrix]


def draw(segments):
    points = set()
    for s in segments:
        points.add((s[0:2]))
        points.add((s[2:4]))
    points = list(points)
    GOAL = [[0] * len(points) for _ in range(len(points))]
    graph = create_matrix(segments, points)
    odd_count = sum([sum(row) % 2 for row in graph])
    if odd_count > 2:
        return []
    for start in points:
        stack = [((start,), copy_matrix(graph))]
        while stack:
            path, state = stack.pop()
            current = path[-1]
            if state == GOAL:
                # print(path)
                return path
            i = points.index(current)
            for j, p in enumerate(state[i]):
                if not p:
                    continue
                new_path = path + (points[j],)
                new_state = copy_matrix(state)
                new_state[i][j] = new_state[j][i] = 0
                stack.append((new_path, new_state))
    return []


def checker(func, indata, is_possible=True):
    user_result = func(indata)
    if not is_possible:
        if user_result:
            print("How did you draw this?")
            return False
        else:
            return True
    if len(user_result) < 2:
        print("More points please.")
        return False
    data = list(indata)
    for i in range(len(user_result) - 1):
        f, s = user_result[i], user_result[i + 1]
        if (f + s) in data:
            data.remove(f + s)
        elif (s + f) in data:
            data.remove(s + f)
        else:
            print("The wrong segment {}.".format(f + s))
            return False
    if data:
        print("You forgot about {}.".format(data[0]))
        return False
    return True


# assert checker(draw, {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)})
# assert checker(draw, {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 1), (7, 5, 1, 2)},
#                False)
# assert checker(draw, {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 1), (7, 5, 1, 2),
#                       (1, 5, 7, 5)})

T = [
#     {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)},
#     {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
#     {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}
# ]

# T = [
    # {(1, 1, 9, 9)},
    # {(1, 1, 1, 99), (99, 99, 99, 1), (99, 99, 1, 99), (99, 1, 1, 1)},
    # {(8, 4, 8, 6), (4, 8, 6, 2), (6, 8, 8, 6), (4, 8, 8, 6), (2, 6, 6, 8), (6, 2, 8, 4), (2, 6, 8, 6), (2, 6, 6, 2),
    #  (2, 4, 8, 4), (6, 8, 8, 4), (4, 2, 6, 2), (4, 2, 8, 6), (2, 4, 2, 6), (4, 2, 6, 8), (4, 2, 4, 8), (2, 4, 6, 2),
    #  (2, 4, 4, 8), (4, 8, 6, 8), (2, 6, 4, 2), (6, 2, 8, 6), (4, 8, 8, 4), (6, 8, 6, 2), (2, 4, 6, 8), (4, 2, 8, 4),
    #  (2, 4, 4, 2), (2, 6, 4, 8), (2, 6, 8, 4), (2, 4, 8, 6)},
    # {(4, 2, 6, 8), (2, 6, 6, 8), (2, 6, 6, 2), (2, 4, 6, 8), (2, 4, 8, 4), (2, 4, 4, 2), (2, 4, 6, 2), (4, 2, 4, 8),
    #  (2, 4, 4, 8), (4, 8, 6, 8), (4, 8, 6, 2), (2, 6, 4, 2), (2, 6, 4, 8), (6, 2, 8, 4), (2, 6, 8, 4), (4, 2, 6, 2),
    #  (4, 8, 8, 4), (4, 2, 8, 4), (2, 4, 2, 6), (6, 8, 8, 4), (6, 8, 6, 2)}
    {
        (3, 3, 50, 50),
        (50, 50, 97, 8),
        (97, 8, 3, 3)
    },
    {
        (10, 20, 10, 30),
        (10, 20, 20, 10),
        (10, 30, 20, 40),
        (20, 40, 30, 40),
        (20, 10, 30, 10),
        (30, 40, 40, 25),
        (30, 10, 40, 25),
        (40, 25, 50, 40),
        (40, 25, 50, 10),
        (50, 10, 60, 10),
        (50, 40, 60, 40),
        (60, 10, 70, 20),
        (60, 40, 70, 30),
        (70, 30, 70, 20)
    },
    {(55, 66, 33, 56), (11, 11, 55, 66), (22, 33, 33, 56), (22, 33, 55, 66), (11, 11, 22, 33)}
,
    {(55, 30, 55, 55), (40, 20, 55, 55), (55, 30, 70, 44), (10, 50, 55, 55), (10, 50, 40, 20), (10, 50, 70, 44), (40, 20, 55, 30), (55, 55, 70, 44), (10, 50, 55, 30), (40, 20, 70, 44)}


]

for t in T:
    is_possible = draw(t)
    lt = list(t)
    print("""{{
    "input": {},
    "answer": {},
    }},""".format(lt, lt if is_possible else []))


def generate_full(points):
    from itertools import combinations

    res = set()
    for f, s in combinations(points, 2):
        res.add(f + s)
    return res


print(generate_full(((2, 4), (2, 6), (4, 2), (4, 8), (6, 8), (6, 2), (8, 4), (8, 6))))
print(generate_full(((2, 4), (2, 6), (4, 2), (4, 8), (6, 8), (6, 2), (8, 4))))
print(generate_full(((11, 11), (22, 33), (55, 66), (33, 56))))
print(generate_full(((10, 50), (40, 20), (55, 30), (55, 55), (70, 44))))