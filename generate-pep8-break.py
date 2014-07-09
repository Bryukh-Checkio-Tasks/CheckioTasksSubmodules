from re import split

P = "?[({#,<;:>.@})]!"


def twist(text):
    text = text.translate(str.maketrans("?[({#,<;:>.@})]!", "?[({#,<;:>.@})]!"[::-1]))
    # print(str.maketrans("?[({#,<>.@})]!", "?[({#,<>.@})]!"[::-1]))
    text = " ".join(w for w in text.split() if w)
    # print(split("(\w+)", text))
    text = "".join("".join(c.lower() if c.isupper() else c.upper() for c in w[::-1]) if w.isalpha() else w
                   for w in split("([a-zA-Z]+)", text))

    text = "".join("".join(str(9 - int(c)) for c in w) if w.isdigit() else w
                   for w in split("(\d+)", text))
    # print(text)
    return text


T = [
    "Hello World!",
    "I'm 1st",
    "How are you? 905th.",
    "The code - ([{<;#>}])",
    "EMAIL        a@b.ru",
    ";-) 0_0 @__@",


]

T = [
    # "",
    # "0123456789",
    # "          ",
    # "A1bc2",
    # "The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. Bright vixens jump; dozy fowl quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs!  Now fax quiz Jack!  my brave ghost pled. Five quacking zephyrs jolt my wax bed. Flummoxed by job, kvetching W. zaps Iraq. Cozy sphinx waves quart jug of bad milk. A very bad quack might jinx zippy fowls. Few quips galvanized the mock jury box. Quick brown dogs jump over the lazy fox. The jay, pig, fox, zebra, and my wolves quack! Blowzy red vixens fight for a quick jump. Joaquin Phoenix was gazed by MTV for luck. A wizard’s job is to vex chumps quickly in fog.",
    # "!#$%&()*+,-./:;<=>?@[\]^_`{|}~",
    "pep8 requirements!?!",
    "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.",
    "9+5*2-1=18",
    "PEP8? I don`t know anything about this."

]

for t in T:
    ans = twist(t)
    print("""{{
        "input": "{}",
        "answer": "{}"
    }},""".format(t, ans))