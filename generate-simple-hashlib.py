import hashlib
import random
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
    hash_text = lambda t, func: hashfunc_dic[func](bytes(t, "utf-8")).hexdigest()
else:
    hash_text = lambda t, func: hashfunc_dic[func](t).hexdigest()