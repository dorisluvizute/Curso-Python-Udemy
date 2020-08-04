# Comeando try, ele tenta fazer algo, e caso não aocnteça ele cria uma excessão
resp = 's'
fatura = []
total = 0
valid = False

while resp == 's':
    produto = input('Digite o nome do produto: ').lower()
    
    while valid == False:
        preço = input('Digite o preço do produto: ')

        try:
            preço = float(preço)
            if preço <= 0:
                print("O preço precisa ser maior que zero")
            else:
                valid = True
        except:
            print("Formato de preço invalido. Use apenas números e separe os centavos com '.'")

    fatura.append([produto,preço])
    total += preço
    valid = False
    resp = input('Deseja comprar mais algum produto? Responda s para sim ou n para não: ' ).lower()

for i in fatura:
    print(i[0],':',i[1])

print('O total da fatura é:',total)