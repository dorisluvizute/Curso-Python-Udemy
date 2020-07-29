# Listas e Tuplas servem pra guardar um conjunto de informações
# São em sequências

# Tupla, uso aspas
meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
print(meses)
print(type(meses))

# Lista, uso colchetes
alunos = ["João","Maria","Pedro","Helena"]
print(alunos)
print(type(alunos))

# Comprimento da Tupla / Lista
print(len(meses))
print(len(alunos))

# Índice da Tupla / Lista
print(meses[0])
print(meses[11])
print(alunos[3])

# A principal diferença entre eles é que as tuplas são imutáveis e as listas mutáveis

# Por exemplo para alterar um nome na Lista:
alunos[1] = "Mariah"
print(alunos)
# Adicionar um nome:
alunos.append("Ricardo")
print(alunos)
# Adicionar um nome em uma posição específica:
alunos.insert(1,"Paula")
print(alunos)
# Colocar em ordem alfabética
alunos.sort()
print(alunos)

# Tirar um nome da lista pelo índice:
alunos.pop(1)
print(alunos)
# Tirar um nome da lista pelo nome:
alunos.remove("Paula")
print(alunos)

# Concatenação de Listas:
alunos2 = ["Joana","Jorge"]
total = alunos + alunos2
print(total)
print(type(total))

print(total[2])

# Também posso buscar um índice na lista através de uma variável com um número guardado
indice = 2
print(total[indice])