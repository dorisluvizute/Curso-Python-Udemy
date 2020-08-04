# Funciona com as sequências
# Ex: listas e strings
compras = ['arroz','feijão','macarrão','carne']

nome = 'joaquim'

for i in compras:
    print(i)

for i in nome:
    print(i)

# Somatório com for loop
vendas = [1000,450,300,920,600]

total = 0

for i in vendas:
    total += i
    print(total)

# for loop com dicionário
cores = {'verde':'green','preto':'black','azul':'blue'}

for i in cores:
    print(i,":",cores[i])

# for loop aninhado
compras = [['arroz','feijão','macarrão'],['carne','frango','peixe'],['leite','yogurte']]

for i in compras:
    for item in i:
      print(item)  

# renge
for i in range (0,10):
    print(i)

for i in range (0,10):
    print(i + 1)

for i in range (0,10):
    print(10 - i)