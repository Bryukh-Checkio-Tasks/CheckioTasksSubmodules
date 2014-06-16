import random

VOWELS = "aeyuio"

def human2bird(phrase):
    words = phrase.split()
    result = []
    for w in words:
        result.append("".join(ch * 3 if ch in VOWELS else ch + random.choice(VOWELS) for ch in w))
    return " ".join(result)

print(human2bird("checkio"))
print(human2bird("checkio"))
print(human2bird("a b c d e f"))