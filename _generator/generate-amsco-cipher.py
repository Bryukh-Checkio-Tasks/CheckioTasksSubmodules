from math import ceil
import random
import string


def encode_amsco(message, key):
    columns = len(str(key))
    ch_in_rows = int(columns * 1.5)
    rows = []
    count = 0
    row = 0
    while count < len(message):
        current = (row % 2) + int(columns * 1.5) if columns % 2 else int(columns * 1.5)
        rows.append(message[count:count + current])
        count += current
        row += 1

    # rows = [message[r * ch_in_rows:(r + 1) * ch_in_rows] for r in range(ceil(len(message) / ch_in_rows))]
    matrix = []
    for r, line in enumerate(rows):
        mark = col = 0
        temp = []
        while mark < len(line):
            if (col + r) % 2:
                temp.append(line[mark:mark + 2])
                mark += 2
            else:
                temp.append(line[mark:mark + 1])
                mark += 1
            col += 1
        matrix.append(temp)
    table = [row[:] for row in matrix]
    matrix[-1].extend([""] * (columns - len(matrix[-1])))
    matrix = [list(row) for row in zip(*matrix)]
    result = [[] for _ in range(columns)]
    # print(matrix)
    for i, str_n in enumerate(str(key)):
        n = int(str_n)
        result[n - 1] = "".join(matrix[i])
    return "".join(result), table


# T = [
#     ["loremipsumdolorsitamet", 4123],
#     ["checkio", 23415],
#     ["howareyouwillhometommorrow", 123]
# ]

PHRASES = [
#     "What on earth does that mean?",
    "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country",
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.",
    "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment.",
    "The quick, brown fox jumps over a lazy dog.",
    "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary",
    "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure"
]

# for t in T:
#     encoded, table = encode_amsco(*t)
#     print("""{{
#     "input": {},
#     "answer": {},
#     "explanation": {}
#     }},""".format([encoded, t[1]], t[0], table))

for _ in range(15):
    ph = "".join(ch.lower() for ch in random.choice(PHRASES) if ch in string.ascii_letters)
    key = list(range(1, random.randint(4, 6)))
    random.shuffle(key)
    key = int("".join(str(x) for x in key))
    encoded, table = encode_amsco(ph, key)
    print("""{{
    "input": {},
    "answer": "{}",
    "explanation": {}
    }},""".format([encoded, key], ph, table))