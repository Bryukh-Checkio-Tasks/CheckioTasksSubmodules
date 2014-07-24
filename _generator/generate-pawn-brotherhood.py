ROWS = "12345678"
COLS = "abcdefgh"

def safe_pawns(pawns):
    safe_cells = set()
    for pc, pr in pawns:
        row = int(pr) - 1
        col = ord(pc) - 97
        if row == 7:
            continue
        if col:
            safe_cells.add(COLS[col - 1] + ROWS[row+1])
        if col < 7:
            safe_cells.add(COLS[col + 1] + ROWS[row+1])
    return len(safe_cells.intersection(pawns))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
