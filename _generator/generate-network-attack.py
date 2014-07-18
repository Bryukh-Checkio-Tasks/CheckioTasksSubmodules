from heapq import heappush, heappop
from random import randint


def capture(matrix):
    queue = []
    heappush(queue, (0, 0))
    for i in range(1, len(matrix)):
        heappush(queue, (float("inf"), i))
    result = {}
    visited = set()
    while queue:
        dist, current = heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        result[current] = dist
        for j, n in enumerate(matrix[current]):
            if current == j or not n or j in visited:
                continue
            level = matrix[j][j]
            heappush(queue, (dist + level, j))
    expl = {}
    for k, v in result.items():
        expl[k] = v - matrix[k][k]
    # print(result)
    # print(expl)
    return max(result.values()), expl


T = [
    # [[0, 1, 0, 1, 0, 1],
    #  [1, 8, 1, 0, 0, 0],
    #  [0, 1, 2, 0, 0, 1],
    #  [1, 0, 0, 1, 1, 0],
    #  [0, 0, 0, 1, 3, 1],
    #  [1, 0, 1, 0, 1, 2]],
    #
    # [[0, 1, 0, 1, 0, 1],
    #  [1, 1, 1, 0, 0, 0],
    #  [0, 1, 2, 0, 0, 1],
    #  [1, 0, 0, 1, 1, 0],
    #  [0, 0, 0, 1, 3, 1],
    #  [1, 0, 1, 0, 1, 2]],
    #
    # [[0, 1, 1],
    #  [1, 9, 1],
    #  [1, 1, 9]],
    #
    [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ],
    [
        [0, 1, 0],
        [1, 9, 1],
        [0, 1, 9],
    ],
    [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 3, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 5, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 6, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 7, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 8, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    ],
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 3, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 4, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 5, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 6, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 7, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 8, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
    ],


]


def generate_test():
    N = randint(3, 10)
    matrix = [[0] * N for _ in range(N)]
    for i in range(1, N):
        matrix[i][i] = randint(1, 9)
    for i in range(N):
        for j in range(i + 1, N):
            k = randint(0, 1)
            matrix[i][j] = k
            matrix[j][i] = k
    return matrix

# for t in T:
for _ in range(10):
    t = generate_test()
    ans, expl = capture(t)
    print("""{{
    "input": {},
    "answer": {},
    "explanation": {},
    }},""".format(t, ans, expl))
