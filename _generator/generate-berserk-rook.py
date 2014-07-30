ROWS = "12345678"
COLS = "abcdefgh"


def berserk_rook(berseker, enemies):
    queue = [(berseker, enemies.copy(), ())]
    best_path, max_killed = "", 0
    N = len(enemies)
    while queue:
        position, state, path = queue.pop()
        if (N - len(state)) > max_killed:
            max_killed = N - len(state)
            best_path = path
        for en in state:
            flag = False
            if en[0] == position[0]:
                sr = min(ROWS.index(position[1]), ROWS.index(en[1]))
                er = max(ROWS.index(position[1]), ROWS.index(en[1]))
                if all((en[0] + ROWS[i]) not in state for i in range(sr + 1, er)):
                    flag = True
            if en[1] == position[1]:
                sc = min(COLS.index(position[0]), COLS.index(en[0]))
                ec = max(COLS.index(position[0]), COLS.index(en[0]))
                if all((COLS[i] + en[1]) not in state for i in range(sc + 1, ec)):
                    flag = True
            if flag:
                new_state = state.copy()
                new_state.remove(en)
                queue.append((en, new_state, path + (en,)))
    return max_killed, best_path




def generate_data(board):
    berserk = None
    enemies = set()
    for i, row in enumerate(board):
        for j, el in enumerate(row):
            if el == "O":
                berserk = COLS[j] + ROWS[-i-1]
            if el == "X":
                enemies.add(COLS[j] + ROWS[-i-1])
    return berserk, enemies

T = [
    # [
    #     "-XX-----",
    #     "--------",
    #     "-X-X--X-",
    #     "--------",
    #     "------X-",
    #     "---O----",
    #     "--------",
    #     "--------"
    # ],
    # [
    #     "-----X-X",
    #     "--------",
    #     "X----X-X",
    #     "--------",
    #     "--------",
    #     "--------",
    #     "O----X--",
    #     "--------"
    # ],
    # [
    #     "-----X--",
    #     "--------",
    #     "X----X-X",
    #     "--------",
    #     "--------",
    #     "--------",
    #     "O----X--",
    #     "--------"
    # ],
    # [
    #     "--------",
    #     "--------",
    #     "--------",
    #     "--O----X",
    #     "--------",
    #     "--------",
    #     "--------",
    #     "--------"
    # ],
    # [
    #     "------X-",
    #     "----X---",
    #     "-X-X----",
    #     "--O-----",
    #     "-X-X----",
    #     "----X---",
    #     "-----X--",
    #     "--------"
    # ],
    # [
    #     "-X--X--X",
    #     "--------",
    #     "--------",
    #     "-X--O--X",
    #     "--------",
    #     "--------",
    #     "-X--X--X",
    #     "--------"
    # ],
    # [
    #     "--------",
    #     "--------",
    #     "--------",
    #     "XXOXXXXX",
    #     "--------",
    #     "--------",
    #     "--------",
    #     "--------"
    # ],
    # [
    #     "----X---",
    #     "--------",
    #     "----X---",
    #     "-------X",
    #     "----X---",
    #     "X-------",
    #     "--X-----",
    #     "X---O--X"
    # ],
    # [
    #     "--------",
    #     "-------X",
    #     "-X--X---",
    #     "X------X",
    #     "----X---",
    #     "--------",
    #     "X---X---",
    #     "-------O"
    # ],
    [
        "---O----",
        "---X---X",
        "--------",
        "---X---X",
        "--------",
        "---X---X",
        "--------",
        "---X---X"
    ],
    [
        "--------",
        "--O-XX--",
        "--XXX---",
        "--XXX---",
        "--------",
        "--------",
        "--------",
        "--------"
    ],
    [
        "--------",
        "--O-XX-",
        "--XX----",
        "--XX----",
        "--XX----",
        "--------",
        "--------",
        "--------"
    ],



]

for t in T:
    indata = generate_data(t)
    ans, expl = berserk_rook(*indata)
    print("""{{
    "input": {},
    "answer": {},
    "explanation": {}
    }},""".format(indata, ans, expl))

# assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5
# assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6
# assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4