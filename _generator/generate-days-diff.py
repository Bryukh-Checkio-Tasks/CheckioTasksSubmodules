from random import shuffle, randint as r


def days_diff(date1, date2):
    from datetime import date
    return abs((date(*date1) - date(*date2)).days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238


T = [
    # ((1982, 4, 19), (1982, 4, 22)),
    # ((2014, 1, 1), (2014, 8, 27)),
    # ((2014, 8, 27), (2014, 1, 1)),
    ((1, 1, 1), (9999, 12, 31)),
    ((9999, 12, 31), (1, 1, 1)),
    ((1970, 1, 1), (2000, 1, 1)),
    ((2014, 2, 28), (2014, 2, 28)),
    ((2012, 2, 29), (2014, 2, 28)),
    ((2012, 2, 29), (2014, 2, 29)),

]

for t in T:
    if t is None:
        t = ((r(1, 9999), r(1, 12), r(1, 31)), (r(1, 9999), r(1, 12), r(1, 31)))
    try:
        ans = days_diff(*t)
    except Exception as ex:
        continue
    print("""{{
    "input": {},
    "answer": {}
    }},""".format(t, ans))