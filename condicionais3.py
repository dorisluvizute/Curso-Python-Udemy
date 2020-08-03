# Uso do Or
# Apertar tab para identar tudo
idade = int(input('Digite sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower()
cidade = input('Digite a sua cidade: ').lower()

if cidade == 'rio' or cidade =='sao paulo':
   
    if sexo == 'm':
        if idade < 18:
            print('Homem menor de idade da regiao sudeste')
        else:
            print('Homen maior de idade da regiao sudeste')

    elif sexo == 'f':
        if idade < 18:
            print('Mulher menor de idade da regiao sudeste')
        else:
            print('Mulher maior de idade da regiao sudeste')

    else:
        print('Erro na entrada de dados')

else:
    print('teste apenas para a região sudeste')