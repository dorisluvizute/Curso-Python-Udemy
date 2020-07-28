nome = "Dóris Andressa"
sobrenomeMãe = "Moura"
sobrenomePai = "Luvizute"

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

palavra = "paralelepípedo"
print(palavra[4:8])