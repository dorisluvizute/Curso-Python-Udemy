# As condicionais carregam a lógica dos programas
# tipo 'boolean' ou bool são as variavéis do tipo verdadeiro ou falso
idade = 18

if idade >= 18:
     print('teste')

# Se eu quiser apenas uma idade tenho que colocar o sinal de = duas vezes

age = int(input('Sua Idade: '))

if age == 18:
    print('A idade é igual a 18')
    print('Dentro do if')

print ('fora do if')    

# Tudo oq tiver dentro do if vai ser o retorno de acordo com a resposta

# O else precisa ser o comando seguinte ao if
# ele coloca uma condição
# O elif coloca outra condição, deve estar entre o if e o else

idade2 = int(input('Sua idade: '))

if idade2 == 18:
    print("A idade é 18")
elif idade2 == 17:
    print("A idade é 17")
else:
    print('A idade não é 17 nem 18')

# para saber se a varíavel é diferente do número que vc deseja use !=
if idade2 != 18:
    print("a idade não é igual a 18")