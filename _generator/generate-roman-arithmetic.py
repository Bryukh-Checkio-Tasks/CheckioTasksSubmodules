SYMBOLS = "IVXLCDM"

def roman():
    'return roman numeral using the specified integer value from range 1...3999'
    units = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    result_dict = {}
    for number in range(1, 4000):
        res = ''
        res += 'M' * (number // 1000)
        res += hundreds[((number // 100) % 10) - 1] if ((number // 100) % 10) else ''
        res += tens[((number // 10) % 10) - 1] if ((number // 10) % 10) else ''
        res += units[(number % 10) - 1] if (number % 10) else ''
        result_dict[res] = number
    return result_dict

ROMAN = roman()

import re

def check_equality(expr):
    elements = re.split("([+-=])", expr)
    for i in range(0, len(elements), 2):
        try:
            elements[i] = ROMAN[elements[i]]
        except KeyError:
            return False
    # print(elements)
    eq = eval("".join(str(x) for x in elements[:-2]))
    return eq == elements[-1]

from itertools import product

def recover(equality):
    unknown = equality.count("?")
    result = ""
    for var in product(SYMBOLS, repeat=unknown):
        eq = equality
        for el in var:
            eq = eq.replace("?", el, 1)
        if check_equality(eq):
            if result:
                return [result, eq]
            else:
                result = eq
    return result


T = [
    "X-??=IV",
    "??+??=X",
    "?+?+?+?+?=L",
    "??-??=?",
    "M?-?=?"
]

for t in T:
    ans = recover(t)
    if isinstance(ans, str):
        explanation = []
    elif isinstance(ans, list):
        explanation = ans
        ans = ""
    else:
        explanation = ["No solutions"]
    print("""
    {{
        "input": "{}",
        "answer": "{}",
        "explanation": {},
    }},""".format(t, ans, explanation))

# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert recover("X-??=IV") == "X-VI=IV", "example 10-6=4"
#     assert recover("??+??=X") == "", "Two solutions"
#     assert recover("?+?+?+?+?=L") == "X+X+X+X+X=L", "Several operands"
#     assert recover("??-??=?") == "", "No solutions"
