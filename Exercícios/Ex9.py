def CopiarEditar(a):
    novo = {}
    for key, value in a.items():
        novo[key] = sum(value)/len(value)

    return novo


notas = {
 'João': [7, 8, 9],
 'Maria': [10, 9, 8],
 'Ana': [6, 7, 8]
}

print(CopiarEditar(notas))