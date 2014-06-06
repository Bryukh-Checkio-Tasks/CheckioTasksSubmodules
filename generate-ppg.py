from random import randint


def is_prime(n):
    for i in range(2, n):
        if not n % i:
            return False
    return True


def golf(number):
    while True:
        number += 1
        # print(number, str(number) == reversed(str(number)), is_prime(number))
        if str(number) == str(number)[::-1] and is_prime(number):
            return number

T = [
    98689,
    98688
]

# for t in T:
for _ in range(10):

    t = randint(1, 10000)
    ans = golf(t)
    print('''{{
    "input": {},
    "answer": {}
}},'''.format(t, ans))