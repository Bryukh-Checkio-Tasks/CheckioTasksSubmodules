def encode(message, key):
    crypt = ""
    # for i, m in enumerate(message):
    #     k_code = ord(key[i % len(key)])
    #     m_code = ord(m)
    return "".join(chr((((ord(m) + ord(key[i % len(key)])) - 130) % 26) + 65) for i, m in enumerate(message))


def decode(old_plain, old_crypt, new_crypt):
    return "???"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    pass



# print(encode("ATTACKATDAWN", "LEMON"))
a = "LXFOPVEFRNHR"

TESTS = [
    # ["DONTWORRYBEHAPPY", "CHECKIO", "BEHAPPYDONTWORRY"],
    # ["HELLO", "HELLO", "BYE"],
    # ["LOREMIPSUM", "DOLORIUM", "LOREMIPSUM"]
]

for old, key, new in TESTS:
    old_crypt = encode(old, key)
    new_crypt = encode(new, key)
    print("""{{
    "input": {},
    "answer": "{}",
    "explanation": "{}",
    }},""".format([old, old_crypt, new_crypt], new, key))

PHRASES = [
    "And now for something completely different.",

    "A nod's as good as a wink to a blind bat, eh?",

    "It's not pining. It's passed on. This parrot is no more."
    " It has ceased to be. It's expired and gone to meet its maker."
    " This is a late parrot. It's a stiff. Bereft of life, it rests in peace."
    " If you hadn't nailed it to the perch, it would be pushing up the daisies."
    " It's rung down the curtain and joined the choir invisible. THIS IS AN EX-PARROT.",

    "Nobody expects the Spanish Inquisition!",

    "Our experts describe you as an appallingly dull fellow, unimaginative, timid, lacking in initiative,"
    " spineless, easily dominated, no sense of humour, tedious company and irrepressibly drab and awful."
    " And whereas in most professions these would be considerable drawbacks, in chartered accountancy "
    "they are a positive boon",

    "All right ... all right ... but apart from better sanitation and medicine and education and"
    " irrigation and public health and roads and a freshwater system and baths and public order ..."
    " what have the Romans ever done for us",

    "He's not the messiah. He's a very naughty boy!",

    " I'm a lumberjack and I'm OK,"
    "I sleep all night and I work all day."
    "I cut down trees, I skip and jump,"
    'I like to press wild flowers.'
    "I put on women's clothing,"
    "And hang around in bars.",

]

KEYS = [
    "PYTHON",
    "MONTY",
    "GUIDO",
    "CHECKIO",
    "JUSTFUN",
    "OOOOOOO",
    "HOHOHOHO",
    "EVERYBODY"
]

import string

def process(message):
    return "".join(ch.upper() for ch in message if ch in string.ascii_letters)

for i in range(min(len(PHRASES), len(KEYS))):
    # key = KEYS[i]
    # old_phrase = process(PHRASES[i])
    # new_phrase = process(PHRASES[-i-1])
    key = KEYS[i]
    old_phrase = process(PHRASES[-i-1])
    new_phrase = process(PHRASES[i])
    old_crypt = encode(old_phrase, key)
    new_crypt = encode(new_phrase, key)
    print("""{{
    "input": {},
    "answer": "{}",
    "explanation": "{}",
    }},""".format([old_phrase, old_crypt, new_crypt], new_phrase, key))
