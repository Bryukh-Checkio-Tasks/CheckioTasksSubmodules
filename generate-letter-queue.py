import random


def letter_queue(commands):
    q = []
    for c in commands:
        if c.startswith("PUSH"):
            q.append(c.split()[1])
        elif q:
            q.pop(0)
    # print(q)
    return "".join(q)

T = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

P = 0.6
import string

for t in T:
    if t is None:
        t = []
        for _ in range(random.randint(1, 30)):
            if random.random() > P:
                t.append("POP")
            else:
                t.append("PUSH " + random.choice(string.ascii_uppercase))
    ans = letter_queue(t)
    print("""   {{
        "input": {},
        "answer": {}
    }},""".format(t, ans))