vendas =  {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
lst = []
counter = 0
for key in vendas:
    lst.append(vendas[key])

venda_total = sum(lst)
print(venda_total)

#ou

for key in vendas:
    counter = counter + vendas[key]

print(counter)