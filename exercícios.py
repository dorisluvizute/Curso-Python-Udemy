# Exercício 1:
nome = "Dóris"
sobrenome_Mae = "Moura"
sobrenome_Pai = "Luvizute"
iniciais = nome[0] + sobrenome_Mae[0] + sobrenome_Pai[0]
print(iniciais)

# Exercício 2:
empresa = "latina"
nome = "doris"
sobrenomePai = "luvizute"
email = nome + "." + sobrenomePai + "@" + empresa + ".com"
print(email)

# Exercício 3:
peso1 = float(input("Digite o peso da primeira prova: "))
peso2 = float(input("Digite o peso da segunda prova: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

resultado1 = (nota1*peso1)+(nota2*peso2)
print("A média do aluno é:", resultado1 / (peso1 + peso2))