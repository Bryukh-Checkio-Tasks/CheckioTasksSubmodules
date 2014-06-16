import random

VOWELS = "aeyuio"

def human2bird(phrase):
    words = phrase.split()
    result = []
    for w in words:
        result.append("".join(ch * 3 if ch in VOWELS else ch + random.choice(VOWELS) for ch in w))
    return " ".join(result)

def tranlate(phrase):
    words = phrase.split()
    result = []
    for w in words:
        i = 0
        temp = ""
        while i < len(w):
            temp += w[i]
            if w[i] in VOWELS:
                i += 3
            else:
                i += 2
        result.append(temp)
    return " ".join(result)

# print(human2bird("checkio"))
# print(human2bird("checkio"))
# print(human2bird("a b c d e f"))

print(tranlate("cuhueeecikuiiiooo"))

T = [
    "lorem ipsum",
    "to be or not to be",
    "bla bla bla bla",
    "do you speak english",
    "i don not understand you"

]

for t in T:
    b = human2bird(t)
    print("""{{
    "input": "{}",
    "answer": "{}"
    }},""".format(b, t))