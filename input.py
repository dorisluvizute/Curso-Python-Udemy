# Iteração do usuário na aplicação
print("Meu primeiro programa em Python")
num1 = input ("Digite um número: ")
num2 = input ("Digite outro número: ")
print("O resultado de",num1,"+",num2,"é:",num1 + num2)
print("Fim do Programa")

# O resultado da errado porque ele faz uma concatenação, reconhece a variavel num1 e num2 como str
print(type(num1))

# Para corrigir tenho que definir como número int
print("Meu primeiro programa em Python")
num1 = int(input ("Digite um número: "))
num2 = int(input ("Digite outro número: "))
print("O resultado de",num1,"+",num2,"é:",num1 + num2)
print("Fim do Programa")

