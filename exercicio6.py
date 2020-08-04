valid1 = False
valid2 = False
valid3 = False

nome = input('Digite seu nome: ')

while valid1 == False:
    nota1 = input('Digite sua nota da prova 1: ')
    try:
        nota1 = float(nota1)
        if 0 <= nota1 <= 10:
            valid1 = True
        else:
            print("Digite apenas núemeros entre 0 e 10")
    except:
        print("Escreva o valor com apenas números e separe com '.'")

while valid2 == False:
    nota2 = input('Digite sua nota da prova 2: ')
    try:
        nota2 = float(nota2)
        if 0 <= nota2 <= 10:
            valid2 = True
        else:
            print("Digite apenas núemeros entre 0 e 10")
    except:
        print("Escreva o valor com apenas números e separe com '.'")

while valid3 == False:
    faltas = input('Digite quantas faltas você teve: ')
    try:
        faltas = int(faltas)
        if 0 <= faltas <= 20:
            valid3 = True
        else:
            print("Digite apenas número entre 0 e 20")
    except:
        print("Escreva o valor com apenas números, sem ',' ou '.'")

media = (nota1 + nota2) / 2
assiduidade = (20 - faltas) / 20

if media >= 6:
    if assiduidade >= 0.7:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ',
              assiduidade, ', ', 'Resultado: Aprovado')
    else:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ',
              assiduidade, ', ', 'Resultado: Reprovado por faltas')

else:
    if assiduidade >= 0.7:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ',
              assiduidade, ', ', 'Resultado: Reprovado por média')
    else:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ',
              assiduidade, ', ', 'Resultado: Reprovado por média e por faltas')
