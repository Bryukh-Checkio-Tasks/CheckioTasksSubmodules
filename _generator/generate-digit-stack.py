import random


def digit_stack(commands):
    q = []
    s = 0
    for c in commands:
        if c.startswith("PUSH"):
            q.append(int(c.split()[1]))
        elif c == "POP":
            s += q.pop() if q else 0
        else:
            s += q[-1] if q else 0
    # print(q)
    return s

# print(letter_queue(['POP', 'PUSH S', 'POP', 'PUSH R', 'POP', 'PUSH B', 'PUSH S', 'POP', 'PUSH U', 'PUSH N', 'PUSH J']))


T = [
    # ['PUSH 0',
    #  'PUSH 1',
    #  'PUSH 2',
    #  'PUSH 3',
    #  'PUSH 4',
    #  'PUSH 5',
    #  'PUSH 6',
    #  'PUSH 7',
    #  'PUSH 8',
    #  'PUSH 9'],
    # ["PEEK"],
    # ["POP"],
    # ['PUSH 0', "PEEK", 'PUSH 1',"PEEK", 'PUSH 2', "PEEK",'PUSH 3', "PEEK",'PUSH 4',"PEEK", 'PUSH 5', "PEEK",'PUSH 6',"PEEK", 'PUSH 7',"PEEK", 'PUSH 8',"PEEK", 'PUSH 9',"PEEK",],
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
        for _ in range(random.randint(1, 20)):
            p = random.random()
            if p > P:
                t.append("PUSH " + random.choice("0123456789"))
            elif p > P * 0.6:
                t.append("POP")
            else:
                t.append("PEEK")
    ans = digit_stack(t)
    print("""   {{
        "input": {},
        "answer": {}
    }},""".format(t, ans))