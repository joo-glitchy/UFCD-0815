def CopiarEditar(a, b):
    junto = {}
    for key, value in a.items():
        junto[key] = value
    for key, value in b.items():
            junto[key] = value

    return junto

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print(CopiarEditar(d1, d2))