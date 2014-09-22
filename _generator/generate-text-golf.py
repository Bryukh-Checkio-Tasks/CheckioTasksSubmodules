from random import randint, random, choice


def golf(text):
    res = []
    for i, row in enumerate(text):
        for j, ch in enumerate(row):
            if text[i][j] != " ":
                continue
            neighs = [(i + x, j + y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y]
            temp = [0 <= x < len(text) and 0 <= y < len(text[x]) and text[x][y] != " " for x, y in neighs]
            if all(temp) and len(temp) == 8:
                res.append([i, j])
    return res


T = [
    # ["How are you doing?",
    #  "I'm fine. OK.",
    #  "Lorem Ipsum?",
    #  "Of course!!!",
    #  "1234567890",
    #  "0        0",
    #  "1234567890",
    #  "Fine! good buy!"],
    # ['Lorem ipsum dolor',
    #  'sit amet,',
    #  'consectetuer',
    #  'adipiscing elit.',
    #  'Aenean commodo',
    #  'ligula eget dolor.',
    #  'Aenean massa. Cum',
    #  'sociis natoque',
    #  'penatibus et magnis',
    #  'dis parturient',
    #  'montes, nascetur',
    #  'ridiculus mus. Donec',
    #  'quam felis,',
    #  'ultricies nec,',
    #  'pellentesque eu,',
    #  'pretium quis, sem.',
    #  'Nulla consequat',
    #  'massa quis enim.',
    #  'Donec pede justo,',
    #  'fringilla vel,'],
    # ["qwerty asdfg ghjkl 123"],
    # ["asd", "0 1"] * 10,
    # ["hi hi"] + ['hello'] * 5 + ["by by"],
    # [
    #     " X ",
    #     "XXX",
    #     " X ",
    #     "X X",
    #     " X "
    # ]
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

from string import ascii_letters

for t in T:
    if t is None:
        h = randint(3, 20)
        w = randint(3, 20)
        t = []
        for _ in range(h):
            t.append(''.join(" " if random() < 0.1 else choice(ascii_letters) for _ in range(randint(5, 20))))
    ans = golf(t)

    print("""{{
        "input": {},
        "answer": {},
        "explanation": {}
        }},""".format(t, len(ans), ans))