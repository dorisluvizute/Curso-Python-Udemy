def imc(peso, altura):
    imc = peso / (altura * altura)
    return(imc)

def class_imc(sexo, peso, altura):
    valor_imc = imc(peso,altura)
    if sexo == 'masculino':
        if valor_imc < 20.7:
            return 'Abaixo do peso.'
        elif 20.7 <= valor_imc < 26.4:
            return 'No peso normal.'
        elif 26.4 <= valor_imc < 27.8:
            return 'Marginalmente acima do peso.'
        elif 27.8 <= valor_imc < 31.1:
            return 'Acima do peso ideal.'
        elif valor_imc >= 31.1:
            return 'Obesidade.'
        else:
            return 'Erro de cálculo.'
    
    elif sexo == 'feminino':
        if valor_imc < 19.1:
             return 'Abaixo do peso.'
        elif 19.1 <= valor_imc < 25.8:
            return 'No peso normal.'
        elif 25.8 <= valor_imc < 27.3:
            return 'Marginalmente acima do peso.'
        elif 27.3 <= valor_imc < 32.3:
            return 'Acima do peso ideal.'
        elif valor_imc >= 32.3:
            return 'Obesidade.'
        else:
            return 'Erro de cálculo.'  
        

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

v_imc = imc(peso, altura)
c_imc = class_imc(sexo, peso, altura)

print('O seu IMC é:', v_imc)
print('A sua classificação é:',c_imc)