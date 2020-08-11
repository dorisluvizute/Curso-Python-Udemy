# Modulos são os arquivos com extensão py
# essas funções são do exercicio7.py

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