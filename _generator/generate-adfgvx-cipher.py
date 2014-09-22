from math import ceil
import random
import string

ADFGVX = "ADFGVX"

def find_letter(table, ch):
    for i, row in enumerate(table):
        for j, el in enumerate(row):
            if el == ch:
                return i, j
    return -1, -1


def encode(message, secret_alphabet1, keyword):
    temp = ""
    for k in keyword:
        temp += k if k not in temp else ""
    keyword = temp
    message = "".join(ch for ch in message.lower() if ch in (string.ascii_letters + string.digits))
    table = [secret_alphabet1[i * 6:(i + 1) * 6] for i in range(6)]
    first = ""
    for ch in message:
        row, col = find_letter(table, ch)
        first += ADFGVX[row] + ADFGVX[col]
    lk = len(keyword)
    s_table = [first[i * lk:(i + 1) * lk] for i in range(ceil(len(first) / lk))]
    s_table[-1] += " " * (len(s_table[0]) - len(s_table[-1]))
    tr_s_table = list(zip(*s_table))
    key_order = sorted((ch, c) for c, ch in enumerate(keyword))
    result = "".join("".join(tr_s_table[j]) for _, j in key_order).replace(" ", "")
    return result

def decode(message, secret_alphabet1, keyword):
    return

# if __name__=='__main__':
#     assert encode('I am going', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') == 'DXGAXAAXXVDDFGFX'
#     # assert decode('DXGAXAAXXVDDFGFX', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','weasel') == 'iamgoing'
#     assert encode('attack at 12:00 am','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','privacy') == 'DGDDDAGDDGAFADDFDADVDVFAADVX'
#     # assert decode('DGDDDAGDDGAFADDFDADVDVFAADVX','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','privacy') == 'attackat1200am'
#     assert encode('ditiszeergeheim','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','piloten') == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA'
#     # assert decode('DFGGXXAAXGAFXGAFXXXGFFXFADDXGA','na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz','piloten') == 'ditiszeergeheim'


PHRASES = [
    # 'I am going',
    # 'attack at 12:00 am',
    # "ditiszeergeheim",
    # 'I am going',
    "One 1, Two 2, Three 3, Four 4, Five 5, Six 6, Seven 7, Eight 8, Nine 9, Zero 0",
    "Your highness, when I said that you are like a stream of bat's piss, I only mean that you shine out like a shaft of gold when all around it is dark",
    "I don't wanna talk to you no more, you empty headed animal food trough wiper! I fart in your general direction! You mother was a hamster and your father smelt of elderberries!",
    "My philosophy, like color television, is all there in black and white",
    "Strange women lying in ponds distributing swords is no basis for a system of government!",
    "We are no longer the knights who say ni! We are now the knights who say ekki-ekki-ekki-pitang-zoom-boing!",
    "Nudge, nudge, wink, wink. Know what I mean?"

]


ALPHABETS = [
    "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
]
KEYS = [
    # "cipher",
    # "privacy",
    # "piloten",
    # "weasel"
    "monty",
    "python",
    "daily",
    "checkio",
    "world",
    "ubermonty",
    "yep"
]

CLOSED = [

]

for i in range(len(KEYS)):
    ph = PHRASES[i]
    al = key1 = list(string.ascii_lowercase + string.digits)
    # al = ALPHABETS[i]
    random.shuffle(al)
    al = "".join(al)
    k = KEYS[-1-i]
    # k = KEYS[i]
    t = [ph, al, k]
    ans = encode(*t)
    CLOSED.append([ans, t[1], t[2]])
    # print(['encode("' + t[0] + '", "' + str(t[1]) + '", "' + str(t[2]) + '")', ans], ",")
    processed = "".join(ch for ch in ph.lower() if ch in (string.ascii_letters + string.digits))
    print(['decode("' + ans + '", "' + str(t[1]) + '", "' + str(t[2]) + '")', processed], ",")