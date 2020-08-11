# Funções guardam um bloco de código para ser reutilizado depois
# Usar def
# .title deixa a primeira letra maiuscula

user = "ivan"

def mensagem(x):
    print('Seja bem-vindo, ' + x.title() + '.')

mensagem(user)

def imc(peso, altura):
    valor_imc = peso / (altura * altura)
    return(valor_imc)


if imc(55,1.64) > 32:
    print('Obesidade')

else:
    print('Saudável')