from random import randint


def convert(numerator, denominator):
    """list[int, int] -> str
    Reformat fraction represented as two integers in repeating decimal
    in brackets format.
    >>> checkio([1, 3])
    '0.(3)'
    >>> checkio([3, 8])
    '0.375'
    >>> checkio([11, 7])
    '1.(571428)'
 
    :param fraction list: Fraction as list - numerator and denominator
    :return str: repeating decimal in brackets format.
    """
    div, mod = divmod(numerator, denominator)
    mod_accumulator = [mod]
    result = [div]
    rstart = 0
 
    while mod:
        mod *= 10
        if mod in mod_accumulator:
            rstart = len(mod_accumulator) - mod_accumulator[::-1].index(mod)
            break
        mod_accumulator.append(mod)
        div, mod = divmod(mod, denominator)
        result.append(div)
    if rstart:
        return (str(result[0]) + "." +
            ''.join([str(d) for d in result[1:rstart - 1]]) + "(" +
            ''.join([str(d) for d in result[rstart - 1:]]) + ")")
    else:
        return str(result[0]) + "." + ''.join([str(d) for d in result[1:]])

def convert2(numerator, denominator):
    """list[int, int] -> str
    Reformat fraction represented as two integers in repeating decimal
    in brackets format.
    >>> checkio([1, 3])
    '0.(3)'
    >>> checkio([3, 8])
    '0.375'
    >>> checkio([11, 7])
    '1.(571428)'

    :param fraction list: Fraction as list - numerator and denominator
    :return str: repeating decimal in brackets format.
    """
    div, mod = divmod(numerator, denominator)
    mod_accumulator = [mod]
    result = [div]
    rstart = 0

    while mod:
        mod *= 10
        if mod in mod_accumulator:
            rstart = len(mod_accumulator) - mod_accumulator[::-1].index(mod)
            break
        mod_accumulator.append(mod)
        div, mod = divmod(mod, denominator)
        result.append(div)
    if rstart:
        return (str(result[0]) + "." +
            ''.join([str(d) for d in result[1:rstart - 1]]) + "(" +
            ''.join([str(d) for d in result[rstart - 1:]]) + ")")
    else:
        return str(result[0]) + "." + ''.join([str(d) for d in result[1:]])

T = [
    [0, 1],
    [0, 1000],
    [1, 1000],
    [1000, 1],
    [1, 999],
    [1, 776]
]
#
# for t in T:
#     ans = convert2(*t)
#     print("""{{
#     "input": {},
#     "answer": "{}"
# }},""".format(t, ans))


for _ in range(10):
    t = randint(1, 1000), randint(1, 1000)
    ans = convert2(*t)
    print("""{{
    "input": {},
    "answer": "{}"
}},""".format(t, ans))
#
# for i in range(1000):
#     print(i)
#     for j in range(1, 1000):
#         a = convert(i, j)
#         print(a)
#         if a != convert2(i, j):
#             print("AHA!!!!!!!!!!!!!!", i, j)