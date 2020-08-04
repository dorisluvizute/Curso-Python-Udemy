# Loops são estruturas de repetição
# Definimos que comandos devem se repetir e por quanto tempo
# Ctrl C sai do loop

# While
x = 0
pessoas = []

# while x < 4:
#     nome = input("Qual o seu nome? ")
#     pessoas.append(nome)
#     x += 1

# print(pessoas)

# 'x += 1' OU 'x = x + 1'

# Para restringir um nome
# while 'joao' not in pessoas:
#     nome = input("Qual o seu nome? ")
#     pessoas.append(nome)

# print(pessoas)

# O joao aparece na lista final, pois o programa le dps de adicionar
# Para não permitir o nome:

# while x < 4:
#     nome = input('Qual o seu nome? ')
#     if nome == 'joao':
#         continue
#     pessoas.append(nome)
#     x += 1

# print(pessoas)

# O continue faz com que saia do loop e volte pro inicio
# O break sai do loop e termina ele

while x < 4:
    nome = input('Qual o seu nome? ')
    if nome == 'joao':
        break
    pessoas.append(nome)
    x += 1

print(pessoas)