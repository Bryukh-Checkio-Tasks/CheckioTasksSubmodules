def count_words(text, words):
    return sum(w in text.lower() for w in words)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start, start + len(sub)
        start += 1


def checkio(text, words):
    lower_copy = text.lower()
    indexes = []
    for w in words:
        indexes.extend(find_all(lower_copy, w))
    indexes.sort()
    prev = 0
    i = 0
    while i < len(indexes) - 1:
        left_index1, right_index1 = indexes[i]
        left_index2, right_index2 = indexes[i+1]
        if left_index2 < right_index1:
            indexes[i] = (left_index1, max(right_index1, right_index2))
            indexes.pop(i+1)
        else:
            i += 1
    result = ""
    for start, end in indexes:
        result += text[prev:start] + "<strong>" + text[start:end] + "</strong>"
        prev = end
    result += text[prev:len(text)]
    return result

T = [
    ["How aresjfhdskfhskd you?", ["how", "are", "you", "hello"]],
    ["Bananas, give me bananas!!!", ["banana", "bananas"]],
    ["Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", ["sum", "hamlet", "infinity", "anything"]]
]

T = [
    ["A", ["the"]],
    ['PWEtRJYqAKYqMcnJxZSStUOyAJkvdtRgdBxnPpXZkBBZXmgatDzedINMmRVxWCIeUfXShDvlWCQtgGYXOxsFpdlNHhxUBRAwAZqXdCkFdjYhBGwpVwJngGxgTDdBHVDdufWGbdENvxbOMylqdPWBiKpptHbXuZwFKBAwCGiXNkWxdHwadOqduygveRsmWfpjEWAztZyoLLJjdeTSHuhJRvUjNDPZyJLseXUROuedMIiudevXESwFjuZACswxnUhm',
     ['the', 'who', "any", 'man', "hey", "box", 'zed']],
]

T = [
    ["LOLOLOLOLOL", ["lol", "olo"]],
    ["Oooooooooooo Thhhhe", ["the", "hey"]],
    ["Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
     ["far", "word", "vokal", "count", "tries"]],
    ["The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps.",
     ["nobody", "hamlet", "sophia", "nikola", "stephan"]],
    ["But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born",
     ["this", "that", "they", "she", "hello", "world"]]
]

for t in T:
    show = "{}, {}".format(t[0], set(t[1]))
    ans = count_words(t[0], set(t[1]))
    expl = checkio(t[0], t[1])
    print("""{{
    "input": {},
    "answer": {},
    "show": "{}",
    "explanation": '{}'
    }},""".format(t, ans, show, expl))