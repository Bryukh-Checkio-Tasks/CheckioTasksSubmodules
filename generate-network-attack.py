from heapq import heappush, heappop


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




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
