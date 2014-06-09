def flatten_dict(d):
    stack = [((), d)]
    result = {}
    while stack:
        path, current = stack.pop()
        if current == {}:
            result["/".join(path)] = ""
        for k, v in current.items():
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

r = flatten_dict({"a": 1, "b": {"c": 2, "D": {}}})
print(r)