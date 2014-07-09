from random import randint
from builtins import print

for _ in range(10):
    t = [randint(1, 9) for i in range(randint(2, 10))]
    # print(t)
    print("""   {{
        "input": {0},
        "answer": {0}
    }},""".format(t))


def swapsort(data):
    array = list(data)
    s = sorted(data)
    i = 0
    result = []
    while s != array:
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            result.append(str(i) + str(i+1))
        if i < len(array) - 1:
            i += 1
        if i == len(array) - 1:
            i = 0
    print(",".join(result))
    return ",".join(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert swapsort((6, 4, 2)) == "01,12,01", "Reverse simple"
    assert swapsort((1, 2, 3, 4, 5)) == "", "All right!"
    assert swapsort((1, 2, 3, 5, 3)) == "54", "One move"
