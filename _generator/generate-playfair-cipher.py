import random
import string

ORDER = string.ascii_lowercase + string.digits
N = 6

def form_keytable(key):
    line = []
    for k in key + ORDER:
        if k not in line:
            line.append(k)
    return [line[i * 6:(i + 1) * 6] for i in range(6)]

def prepare_text(text):
    text = text.lower()
    text = "".join(ch for ch in text if ch in ORDER)
    processed = []
    i = 0
    while i < len(text):
        fch = text[i]
        if i == len(text) - 1:
            processed.append(fch + ("z" if fch != "z" else "x"))
            break
        if fch == text[i + 1]:
            processed.append(fch + ("x" if fch != "x" else "z"))
            i += 1
        else:
            processed.append(fch + text[i + 1])
            i += 2
    return processed

def find_letter(table, letter):
    """
    Find letter in the table.
    Precondition: the letter exists in the table
    """
    for i, row in enumerate(table):
        if letter in row:
            return i, row.index(letter)
    return None, None

def encode(message, key):
    digraphs = prepare_text(message)
    key_table = form_keytable(key)
    result = ""
    for di in digraphs:
        row1, col1 = find_letter(key_table, di[0])
        row2, col2 = find_letter(key_table, di[1])
        if row1 == row2:
            en_di = key_table[row1][(col1 + 1) % N] + key_table[row2][(col2 + 1) % N]
        elif col1 == col2:
            en_di = key_table[(row1 + 1) % N][col1] + key_table[(row2 + 1) % N][col2]
        else:
            en_di = key_table[row1][col2] + key_table[row2][col1]
        result += en_di
    return result



def decode(message, key):
    digraphs = [message[i:i + 2] for i in range(0, len(message), 2)]
    key_table = form_keytable(key)
    result = ""
    for di in digraphs:
        row1, col1 = find_letter(key_table, di[0])
        row2, col2 = find_letter(key_table, di[1])
        if row1 == row2:
            en_di = key_table[row1][(col1 - 1) % N] + key_table[row2][(col2 - 1) % N]
        elif col1 == col2:
            en_di = key_table[(row1 - 1) % N][col1] + key_table[(row2 - 1) % N][col2]
        else:
            en_di = key_table[row1][col2] + key_table[row2][col1]
        result += en_di
    return result

PHRASES = [
    # ["Fizz Buzz is x89 XX.", "checkio101"],
    # ["How are you?", "hello"],
    # ["My name is Alex!!!", "Alexander"],
    # ["Who are you?", "human"],
    # ["ATTACK AT DAWN", "general"]
    "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country",
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.",
    "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment.",
    "The quick, brown fox jumps over a lazy dog.",
    "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary",
    "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure"

]

KEYS = [
    "data",
    "goodmorming",
    "iddqd",
    "nobody",
    "9876543210",
    "xyzqwerty"
]

CLOSED = [

]

for i in range(len(KEYS)):
    ph = PHRASES[i]
    k = KEYS[5 - i]
    t = [ph, k]
    ans = encode(*t)
    CLOSED.append([ans, t[1]])
    # print(['encode("' + t[0] + '", "' + str(t[1]) + '")', ans], ",")
    print(['decode("' + ans + '", "' + str(t[1]) + '")', decode(ans, t[1])], ",")

print(encode("Astrologers proclaim month of the Cryptographer. Population of ciphers grows", "checkio"))
print(decode("lyxmcrijonvlxjasgcrtrhmuecbvekol1lxhjqfleklqkrsnbsocreakkqeklxjqixty", "checkio"))