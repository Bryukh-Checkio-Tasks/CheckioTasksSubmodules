from random import randint


def recognize(number):
    signals = [x for x in bin(number)[2:].split("0") if x]
    return all(len(signals[0]) == len(s) for s in signals), bin(number)[2:]

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert recognize(21) == True, "First example"
#     assert recognize(1587) == True, "Second example"
#     assert recognize(3687) == False, "Thid example"


T = {
    "Basic": [
        21,
        1587,
        3687
    ],
    "Extra": [
        1057222719,
        1057222687,
        1,
        1,
        0,
        0,
        1,
        1,
        1,
        0,
        0,
        1,
        0
    ]
}
print("TESTS = {")

for cat in T:
    print("    '{}': [".format(cat))
    for t in T[cat]:
        if t == 1:
            n = randint(1, 6)
            s = "1" * n + randint(1, 6) * "0" + "1" * n + randint(1, 6) * "0" + "1" * n
            t = int(s, 2)
        if t == 0:
            s = "1" * randint(1, 6) + randint(1, 6) * "0" + "1" * randint(1, 6) + randint(1, 6) * "0" + "1" * randint(1, 6)
            t = int(s, 2)
        ans, exp = recognize(t)
        print("""       {{
        "input": {},
        "answer": {},
        "explanation": "{}"
    }},""".format(t, ans, exp))
    print("],")
print("}")