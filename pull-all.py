from plumbum import local, ProcessExecutionError

import os
from os import path

git = local["git"]
ls = local["ls"]
cd = local["cd"]

def pull(dir):
    local.cwd.chdir(dir)
    print(local.cwd)
    try:
        print(git("pull"))
    except ProcessExecutionError as er:
        print(er)
    local.cwd.chdir("..")

def find_dirs(root=".", name=None):
    result = []
    for f in os.listdir(root):
        p = path.join(root, f)
        if path.isdir(p):
            if name:
                if f.startswith(name):
                    result.append(p)
            else:
                if path.isdir(p) and not f.startswith(".") and not f.startswith("_"):
                    result.append(p)
    return result



for dir_name in find_dirs():
    pull(dir_name)