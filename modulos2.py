# Modulos com funções já prontas do python
import math

print(math.ceil(3.2))
# arredonda para cima

print(math.floor(3.7))
# arredonda para baixo

print(math.fsum([1,2,3]))
# pede uma lista e soma os números dela

print(math.sqrt(16))
# te imprime a raiz quadrada do número


import time as t
# módulo que lida com horário e data

print(t.localtime())
# imprime todos os dados de hora

print(t.localtime().tm_mday)
# pega um dado específico fornecido

hora = t.localtime().tm_hour
minuto = t.localtime().tm_min
print('A transação foi feita às ' + str(hora) + 'h e ' + str(minuto) + 'min')

print(t.perf_counter())
# função que conta os segundos de uma ação

def tempo():
    inicio = t.perf_counter()
    print(input('Escreva seu nome: '))
    fim = t.perf_counter()
    contagem = round(fim - inicio,2)
    return 'Você escreveu seu nome em ' + str(contagem) + 'seg'
# função round arredonda em quantos digitos a gnt quer

# print(tempo())

import random
# função que pega numeros aleatórios

print(random.randint(0,10))

# exemplo de utilização do random.randint
def megasena():
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1,60)
        if num in jogo:
            continue
        else:
            jogo.append(num)
    return sorted(jogo)

print(megasena())
# função sorted ordena lista

alunos = ['joão','pedro','maria','helena','guilherme']
# função choice pede uma lista, uma sequência
print(random.choice(alunos))