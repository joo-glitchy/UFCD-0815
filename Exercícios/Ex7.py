def CopiarEditar(a):
    novo = {}
    for key, value in a.items():
        
        novo[value] = key
    return novo

d = {'a': 1, 'b': 2, 'c':3}

print(CopiarEditar(d))