resposta = 's'
fatura = []
total = 0

while resposta == 's':
    produto = input('Digite o nome do produto: ').lower()
    preço = float(input('Digite o preço do produto: '))
    fatura.append([produto,preço])
    total += preço
    resposta = input('Deseja comprar mais algum produto? Responda s para sim ou n para não: ' ).lower()

for i in fatura:
    print(i[0],':',i[1])

print('O total da fatura é:',total)
