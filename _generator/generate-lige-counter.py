NEIGHBOURS = ((-1, -1), (-1, 0), (-1, 1), (0, 1),
              (0, -1), (1, -1), (1, 0), (1, 1))


def convert_grid(matrix):
    grid = {}
    for i, row in enumerate(matrix):
        grid[i] = {}
        for j, el in enumerate(row):
            if el:
                grid[i][j] = el
    print(grid)
    return grid


def clear_grid(g):
    for i in g:
        for j in g[i]:
            if not g[i][j]:
                del (g[i][j])
    for i in g:
        if g[i] == {}:
            del (g[i])


def process_grid(grid):
    born_grid = {}
    died = set()
    for i in grid.keys():
        row = grid[i]
        for j in row.keys():
            neighbours_count = 0
            for di, dj in NEIGHBOURS:
                ni, nj = i + di, j + dj
                if ni in grid and nj in grid[i]:
                    neighbours_count += 1
                if ni not in born_grid[i]:
                    born_grid[ni] = {}
                born_grid[ni][nj] = born_grid[ni].get(nj, 0) + 1
            born_grid[i][j] = 0
            if neighbours_count not in (2, 3):
                died.add((i, j))
    new_grid = {}
    for i in born_grid.keys():
        row = born_grid[i]
        new_grid[i] = {}
        for j in row.keys():
            if grid[i][j]:
                new_grid[i][j] = 0 if (i, j) in died else 1
            else:
                if born_grid[i][j] == 3:
                    new_grid[i][j] = 1
    clear_grid(new_grid)
    draw_grid(new_grid)
    return new_grid


def life_counter(initial, tick_n):
    grid = convert_grid(initial)
    for _ in range(tick_n):
        grid = process_grid(grid)
    return 0


assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                     (0, 0, 1, 0, 0, 0, 0),
                     (1, 1, 1, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 1, 1),
                     (0, 0, 0, 0, 0, 1, 1),
                     (0, 0, 0, 0, 0, 0, 0),
                     (1, 1, 1, 0, 0, 0, 0),), 4) == 15