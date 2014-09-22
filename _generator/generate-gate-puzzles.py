import re
from fractions import Fraction as Fr


def find_word(message):
    words = re.findall("\w+", message.lower())
    result = []
    table = [[0] * len(words) for i in range(len(words))]
    for i, w1 in enumerate(words):
        coefficents = []
        for j, w2 in enumerate(words):
            coef = Fr(0)
            if i == j:
                continue
            coef += 10 * ((w1[0] == w2[0]) + (w1[-1] == w2[-1]))
            coef += (Fr(min(len(w1), len(w2))) / Fr(max(len(w1), len(w2)))) * 30
            coef += (Fr(len(set(w1).intersection(w2))) / Fr(len(set(w1 + w2)))) * 50
            table[i][j] = coef
            coefficents.append(coef)
        result.append((w1, sum(coefficents) / len(coefficents)))
    # print(dict((w, float(f)) for w, f in result))
    ztable = zip(*table)
    for i, row in enumerate(table):
        print(words[i], [round(float(el), 3) for el in row])
    print([sum(round(float(el), 3) for el in col) for col in ztable])
    return max(result, key=lambda x: (round(x[1], 8), words.index(x[0]))), dict((w, float(f)) for w, f in result)

find_word("Friend Fred and friend Ted.")



import string, re
def find_word2(message):
    words = list(map(str.lower, re.findall(r'[a-zA-Z]+', message)))
    res = 0
    co = {}
    for A in words:
        r = 0
        for B in words:
            if A[0] == B[0]:
                r += 10
            if A[-1] == B[-1]:
                r += 10
            p = min(len(A), len(B))
            q = max(len(A), len(B))
            r += 30 * p / q
            common = set(A)&set(B)
            unique = set(A)|set(B)
            r += 50 * len(common) / len(unique)
        co[A] = r / len(words)
        if r >= res or res-r < 1e-5:
            res = r
            ans = A
    print(co)
    return ans

# print(find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. I Narvi made them. Celebrimbor of Hollin drew these signs"))
# find_word("these tfsde durin")
# find_word2("these tfsde durin")


TESTS = [
    # "Speak friend and enter.",
    # "Beard and Bread",
    # "The Doors of Durin, Lord of Moria. Speak friend and enter. I Narvi made them. Celebrimbor of Hollin drew these signs",
    # "Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy. According to a researcher at Cambridge University."
    # "One, two, two, three, three, three."

    "All that is gold does not glitter,",
    "Not all those who wander are lost;",
    "The old that is strong does not wither,",
    "Deep roots are not reached by the frost.",
    "From the ashes a fire shall be woken,",
    "A light from the shadows shall spring;",
    "Renewed shall be blade that was broken,",
    "The crownless again shall be king.",

    "I don't know half of you half as well as I should like;"
    " and I like less than half of you half as well as you deserve.",

    "Fantasy is escapist, and that is its glory. "
    "If a soldier is imprisioned by the enemy, "
    "don't we consider it his duty to escape?. "
    "If we value the freedom of mind and soul, "
    "if we're partisans of liberty, then it's our "
    "plain duty to escape, and to take as many people with us as we can!"

]

for t in TESTS:
    ans, exp = find_word(t)
    # print(ans[0])
    print("""{{
    "input": "{}",
    "answer": "{}",
    "explanation": {},
    }},""".format(t, ans[0], exp))
