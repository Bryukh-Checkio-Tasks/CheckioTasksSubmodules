import hashlib
import random
import string
from sys import version_info as version

hashfunc_dic = {
    "md5": hashlib.md5,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "sha1": hashlib.sha1
}

if version.major == 3:
    hash_text = lambda t, func: hashfunc_dic[func](bytes(t, "utf8")).hexdigest()
else:
    hash_text = lambda t, func: hashfunc_dic[func](t).hexdigest()

T = [
    # 'welcome to pycon',
    # "",
    # None,
    # "Пароль",
    "密码"
    ]

for t in T:
    for alg, f in hashfunc_dic.items():
        if t is None:
            t1 = "".join(random.choice(string.ascii_letters) for _ in range(1024))
        else:
            t1 = t
        ans = f(bytes(t1, "utf8")).hexdigest()
        print("""{{
        "input": ['{}', '{}'],
        "answer": '{}'
}},""".format(t1, alg, ans))