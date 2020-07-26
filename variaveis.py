# Variável: serve para armazenar um valor na memória, atribui um nome a esse valor para ser usado posteriormente
minha_idade = 19
print("Eu tenho",minha_idade,"anos")

# Eu não posso começar uma variável com número, SyntaxError
# Eu não posso usar espaço
# Não posso usar letras maiúsculas, o Python não identifica
# Nomes autoexplicativos são mais fáceis de reconhecer

taxaUSD = 3.20
valor = 300 / taxaUSD
print(valor)

# Variáveis muito longas podem ser ruins para reescrever depois, tentar criar variáveis curtas mas autoexplicativs
# Não usar varíaveis com o mesmo nome das keywords do python (https://www.w3schools.com/python/python_ref_keywords.asp)
# Usar o mesmo nome de varíavel, uma com letra maiúscula e outra com minúscula, com valores diferentes pode causar confusão
# No python não é necessário antes de inicar o programa declarar nenhuma variável nem dizer o tipo

meuNome = "Dóris"
print(meuNome)

# Comando 'type' serve para te mostrar qual o tipo da váriavel
print(type(meuNome))
print(type(taxaUSD))
print(type(minha_idade))

print("Meu primeiro programa em Python")
Num1 = 100
Num2 = 350
print("O resultado de",Num1,"+",Num2,"é:",Num1 + Num2)

# Variaveis do tipo Strings usar "aspas"
# Variaveis do tipo string os sinais vão juntar as palavras sem espaço
nome = "Dóris Andressa"
print(type(nome))
sobrenomeMãe = "Moura"
sobrenomePai = "Luvizute"
print(nome + sobrenomeMãe + sobrenomePai)

# Para usar os sinais e ter espaço tenho que montar o código assim:
print(nome + " " + sobrenomeMãe + " " + sobrenomePai)

# As variaveis do tipo str * int repete a palavra com o número de vezes colocado:
print(nome * 5)

# Os sinais de - ou / não funcionam com srt
# print(nome - D)

# A função len mostra quantos caracteres tem uma variavel
print(len(nome))
print(len(sobrenomeMãe))

# Para pegar o índice de cada caracter dentro de uma str, começa com 0
print(sobrenomeMãe[0])
print(sobrenomeMãe[1])
print(sobrenomeMãe[2])
print(sobrenomeMãe[3])
print(sobrenomeMãe[4])

# Para pegar o índice de cada caracter dentro de uma str de trás pra frente usamos números negativos, começa com -1
print(sobrenomeMãe[-1])
print(sobrenomeMãe[-2])

# Para pegar um grupos de letras da variavel eu tenho que pegar o primeiro número e um após até onde eu quero
# Por exemplo o "Mo" de Moura, tenho que pegar o "M" que é o "0", e o "O" que seria o "1" se torna o "2"
print(sobrenomeMãe[0:2])

print(sobrenomeMãe[0:5])

print(sobrenomeMãe[0:4])
# ou
print(sobrenomeMãe[:4])

# O mesmo com as últimas letras
print(sobrenomeMãe[-2:])
