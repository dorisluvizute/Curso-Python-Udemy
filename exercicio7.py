import modulos
# posso usar outro nome, como: "import modulo as m"

valid = False
valid2 = False
valid3 = False

print('Vamos calcular seu Índice de Massa Corporal?')

while valid == False:
    sexo = input('Informe seu gênero (Feminino ou Masculino): ').lower()
    if sexo == 'feminino' or sexo == 'masculino':
        valid = True
    else:
        print('Sexo inválido.')


while valid2 == False:
    peso = input('Informe seu peso: ')
    try:
        peso = float(peso)
        if 0 <= peso <= 350:
            valid2 = True
        else:
            print('Peso inválido. Escreva números maiores que 0 e menores que 350') 
    except:
       print("Escreva o valor com apenas números e separe com pontos.")

while valid3 == False:
    altura = input('Informe sua altura: ')
    try:
        altura = float(altura)
        if 0 <= altura <= 3:
            valid3 = True
        else:
            print('Altura inválida. Escreva números maiores que 0 e menores que 3 metros.')     
    except:
        print("Escreva o valor com apenas números e separe com pontos.")

v_imc = modulos.imc(peso, altura)
c_imc = modulos.class_imc(sexo, peso, altura)
# Se eu tivesse usado outro nome pro módulo colocaria: "m.imc"

print('O seu IMC é:', v_imc)
print('A sua classificação é:',c_imc)