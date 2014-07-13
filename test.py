def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
 
    if array:
        i = 0
        sumarray = []
        for num in array:
            if i%2 == 0:
                sumarray.append(array[i])
            i+=i
        summed = sum(sumarray)
        end = len(array) - 1
        answer = summed * array[end]
        return answer
    if not array:
        answer = 0
        return answer
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "Empty"