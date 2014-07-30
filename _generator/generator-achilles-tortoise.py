from random import randint


def chase(a1_speed, t2_speed, advantage):
    s0 = t2_speed * advantage
    a0 = t2_speed * s0 / a1_speed
    distance = a0 / (1 - t2_speed / a1_speed)
    return (distance + s0) / t2_speed

T = [
    # [6, 3, 2],
    # [10, 1, 10],
    # [2, 1, 1],
    # [342, 1, 60],
    # [342, 341, 1],
    # [342, 341, 60],
    None,
    None,
    None,
    None,
    None,

]

for t in T:
    if t is None:
        a1 = randint(1, 342)
        t2 = randint(1, a1 - 1)
        adv = randint(1, 60)
        t = [a1, t2, adv]
    ans = chase(*t)
    print("""{{
    "input": {},
    "answer": {}
    }},""".format(t, round(ans, 9)))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"

