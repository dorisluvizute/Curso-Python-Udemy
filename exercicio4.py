nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua nota da prova 1: '))
nota2 = float(input('Digite sua nota da prova 2: '))
faltas = int(input('Digite quantas faltas você teve: '))

media = (nota1 + nota2) / 2
assiduidade = (20 - faltas) / 20

if media >= 6:
    if assiduidade >= 0.7:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ', assiduidade, ', ', 'Resultado: Aprovado')
    else:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ', assiduidade, ', ', 'Resultado: Reprovado por faltas')

else:
    if assiduidade >= 0.7:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ', assiduidade, ', ', 'Resultado: Reprovado por média')
    else:
        print(nome, ', ', 'Média: ', media, ', ', 'Assiduidade: ', assiduidade, ', ', 'Resultado: Reprovado por média e por faltas')