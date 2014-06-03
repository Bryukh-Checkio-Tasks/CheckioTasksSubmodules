from itertools import permutations

def golf(holes):
    best = float("inf")
    route = []
    for var in permutations(holes):
        prev = (0, 0)
        dist = 0
        for h in var:
            dist += ((prev[0] - h[0]) ** 2 + (prev[1] - h[1]) ** 2) ** 0.5
            prev = h
        if dist < best:
            best = dist
            route = var
    return best, route

print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}))